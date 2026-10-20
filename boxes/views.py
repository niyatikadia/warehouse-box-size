# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Box, Order
from .services import find_best_box

@api_view(['POST'])
def recommend_box(request):
    order_id = request.data.get('order_id')
    order = Order.objects.get(id=order_id)

    total_weight = sum(i.product.weight * i.quantity for i in order.items.all())
    # simplification: sabse bade item ka dimension use karo
    biggest = max(order.items.all(), key=lambda i: i.product.length * i.product.width * i.product.height)

    boxes = Box.objects.all()
    best = find_best_box(biggest.product.length, biggest.product.width,
                          biggest.product.height, total_weight, boxes)

    if best is None:
        return Response({"error": "No suitable box found"}, status=404)

    return Response({
        "box": best.name,
        "cost": str(best.cost),
        "max_weight": best.max_weight
    })