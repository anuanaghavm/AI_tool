import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Payment
import json
import hmac
import hashlib

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@csrf_exempt
def create_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)

        name = data.get("name")
        email = data.get("email")
        student_uuid = data.get("student_uuid")
        retest = data.get("retest", False)

        base_amount = 199
        gst = 0.18
        gst_amount = base_amount*gst  # 18% GST = ₹35.82
        final_amount = base_amount+gst_amount  # ₹234.82

        razorpay_amount = int(final_amount * 100)  # in paisa

        # Create Razorpay Order
        razorpay_order = client.order.create({
            "amount": razorpay_amount,
            "currency": "INR",
            "payment_capture": "1"
        })

        # Save to DB
        payment = Payment.objects.create(
            name=name,
            email=email,
            student_uuid=student_uuid,
            retest=retest,
            amount=final_amount,
            gst_amount=gst_amount,
            razorpay_order_id=razorpay_order['id']
        )

        return JsonResponse({
            "order_id": razorpay_order['id'],
            "razorpay_key": settings.RAZORPAY_KEY_ID,
            "amount": final_amount,
            "currency": "INR"
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
            payment.status = 'paid'
            payment.save()
            return JsonResponse({"status": "Payment verified successfully!"})
        else:
            payment.status = 'failed'
            payment.save()
            return JsonResponse({"status": "Payment verification failed"}, status=400)
