from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    razorpay_signature = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, default='created')  # created, paid, failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
