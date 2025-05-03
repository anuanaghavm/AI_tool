from rest_framework import serializers
from .models import Payment,PaymentAmount

class PaymentAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentAmount
        fields = "__all__"
        
class PaymentSerializer(serializers.ModelSerializer):
    student_uuid = serializers.UUIDField(source='student.student_uuid', read_only=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Payment
        fields = [
            'id',
            'student_uuid',
            'name',
            'email',
            'amount',
            'gst_amount',
            'payment_status',
            'razorpay_order_id',
            'razorpay_payment_id',
            'razorpay_signature',
            'created_at'
        ]

