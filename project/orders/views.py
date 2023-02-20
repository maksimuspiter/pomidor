from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrders
from orders.serializer import OrderSerializer


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrders.objects.all()})


class OrderView(ModelViewSet):
    queryset = SalesOrders.objects.all()
    serializer_class = OrderSerializer

def orders_app(request):
    return render(request, 'main_app.html')