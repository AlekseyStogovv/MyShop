from django.urls import path
from . import views
from .aplication import webhooks

# from . import webhooks

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_process, name='completed'),
    path('canceled/', views.payment_process, name='canceled'),
    path('webhook/', webhooks.stripe_webhook, name='stripe-webhook'),
]