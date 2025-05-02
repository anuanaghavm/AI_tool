import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Payment
import json
import hmac
import hashlib
from students.models import Student
from .serializers import PaymentSerializer

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@csrf_exempt
def create_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)

        name = data.get("name")
        email = data.get("email")
        student_uuid = data.get("student_uuid")
        terms_condition = data.get("terms_condition", False)

        # ✅ Get Student object using UUID
        student = get_object_or_404(Student, student_uuid=student_uuid)

        base_amount = 1999
        gst = 0.18
        gst_amount = base_amount * gst
        final_amount = base_amount + gst_amount
        razorpay_amount = int(final_amount * 100)

        # Create Razorpay order
        razorpay_order = client.order.create({
            "amount": razorpay_amount,
            "currency": "INR",
            "payment_capture": "1"
        })

        # Save Payment
        payment = Payment.objects.create(
            student=student,
            name=name,
            email=email,
            terms_conditions=terms_condition,
            amount=final_amount,
            gst_amount=gst_amount,
            razorpay_order_id=razorpay_order['id'],
            payment_status='unpaid'
        )

        return JsonResponse({
            "order_id": razorpay_order['id'],
            "razorpay_key": settings.RAZORPAY_KEY_ID,
            "amount": final_amount,
            "payment_status": payment.payment_status  # ✅ Included here
        })


@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        razorpay_order_id = data.get("razorpay_order_id")
        razorpay_payment_id = data.get("razorpay_payment_id")
        razorpay_signature = data.get("razorpay_signature")

        generated_signature = hmac.new(
            settings.RAZORPAY_KEY_SECRET.encode(),
            f"{razorpay_order_id}|{razorpay_payment_id}".encode(),
            hashlib.sha256
        ).hexdigest()

        payment = get_object_or_404(Payment, razorpay_order_id=razorpay_order_id)

        if generated_signature == razorpay_signature:
            payment.razorpay_payment_id = razorpay_payment_id
            payment.razorpay_signature = razorpay_signature
            payment.payment_status = 'paid'
            payment.save()
            return JsonResponse({"status": "Payment verified successfully!"})
        else:
            payment.payment_status = 'failed'
            payment.save()
            return JsonResponse({"status": "Payment verification failed"}, status=400)


@csrf_exempt
def get_all_payments(request):
    if request.method == "GET":
        payments = Payment.objects.all().order_by('-created_at')
        serializer = PaymentSerializer(payments, many=True)
        return JsonResponse({"payments": serializer.data}, safe=False)

