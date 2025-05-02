from django.db import models
import uuid
from students.models import Student

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('failed','Failed'),
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ]
    student = models.ForeignKey(Student, to_field='student_uuid', on_delete=models.CASCADE, related_name='payments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.TextField()
    terms_conditions = models.BooleanField(default=False)
    amount = models.FloatField()  # final amount with GST
    gst_amount = models.FloatField(default=0.0)
    razorpay_order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    razorpay_signature = models.CharField(max_length=100, blank=True)
    payment_status = models.CharField(max_length=20,choices=PAYMENT_STATUS_CHOICES,default='unpaid')  
    status = models.CharField(max_length=20, default='created')  # created, paid, failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
