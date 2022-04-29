from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
                path('process/', views.payment_process, name='process'),
                path('done/', views.payment_done, name='done'),
                path('canceled/', views.payment_canceled, name='canceled'),
                path('v1/notification', views.YandexNotification.as_view(), name='payment_notification'),
                ]