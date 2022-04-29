from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from new_shop.settings import ALLOWED_HOSTS, YOOKASSA_ACCOUNT_ID, YOOKASSA_SECRET_CODE
from orders.models import Order



import uuid

from yookassa import Configuration, Payment

Configuration.account_id = YOOKASSA_ACCOUNT_ID
Configuration.secret_key = YOOKASSA_SECRET_CODE


@csrf_exempt
def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    payment = Payment.create({
        "amount": {
            "value": total_cost,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"https://{ALLOWED_HOSTS[0]}/payment/done/"
        },
        "capture": True,
        "description": "Заказ №1",
        "metadata": {
            "order_id": order_id
        }
    }, uuid.uuid4())
    order.payment_id = payment.id
    order.save()
    print(payment.id)
    return redirect(payment.confirmation.confirmation_url)


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')


class YandexNotification(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request)
        payment = request.data['object']
        if payment['test']:
            if payment['status'] == 'succeeded':
                order = get_object_or_404(Order, payment_id=payment['id'])
                order.paid = payment['paid']
                order.save()
        return Response(status=200)


