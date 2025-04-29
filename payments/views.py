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
        amount = int(data.get("amount")) * 100  # multiply for Razorpay API (paise)

        # Create Razorpay Order
        razorpay_order = client.order.create({
            "amount": amount,
            "currency": "INR",
            "payment_capture": "1"
        })

        # Save order in DB
        payment = Payment.objects.create(
            name=name,
            email=email,
            amount=amount / 100,   # Save in rupees in database
            razorpay_order_id=razorpay_order['id']
        )

        return JsonResponse({
            "order_id": razorpay_order['id'],
            "razorpay_key": settings.RAZORPAY_KEY_ID,
            "amount": amount / 100,   # Show in rupees to client
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
