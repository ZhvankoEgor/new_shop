from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    # path('my_orders/', views.MyOrders.as_view, name='my_orders'),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
]