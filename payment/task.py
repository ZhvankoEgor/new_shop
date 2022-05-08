from io import BytesIO
from new_shop.celery import app
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@app.task
def payment_completed(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    # create invoice e-mail
    subject = f'Онлайн магазин номер заказа {order.id}'
    message = 'Благодарим вас за покупку, оплаченый счёт находится во вложении'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'Заказ_{order.id}.pdf', out.getvalue(), 'application/pdf')
    # send e-mail
    email.send()
