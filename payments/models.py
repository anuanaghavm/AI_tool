from django.db import models
import uuid

class Payment(models.Model):
    student_uuid = models.UUIDField(default=uuid.uuid4)  # Or you can accept this from the request
    name = models.CharField(max_length=100)
    email = models.EmailField()
    retest = models.BooleanField(default=False)
    amount = models.FloatField()  # final amount with GST
    gst_amount = models.FloatField(default=0.0)
    razorpay_order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    razorpay_signature = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, default='created')  # created, paid, failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
