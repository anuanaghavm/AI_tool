from django.urls import path
from . import views
from.views import PaymentAmountListCreateAPIView,PaymentAmountRetrieveUPdateDestroyAPIView

urlpatterns = [
    path('create-payment/', views.create_payment, name='create_payment'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
    path('payments/',views.get_all_payments,name='getall-payments'),
    path('payment-amount/',PaymentAmountListCreateAPIView.as_view(),name="payment-amount-create"),
    path("payment-amount/<int:pk>/",PaymentAmountRetrieveUPdateDestroyAPIView.as_view(),name="payment-amount-retrieve-update-destroy"),
]
