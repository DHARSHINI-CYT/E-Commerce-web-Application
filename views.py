from django.http import JsonResponse
from .models import Product
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_products(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        p = Product.objects.create(
            name=data.get('name', 'New Product'),
            description=data.get('description', ''),
            price=data.get('price', 0.0),
            sku=data.get('sku', 'SKU-NEW'),
            stock=data.get('stock', 0),
            image_url=data.get('image_url', 'https://via.placeholder.com/800'),
            badge=data.get('badge')
        )
        return JsonResponse(p.to_dict())
    
    products = Product.objects.all()
    return JsonResponse([p.to_dict() for p in products], safe=False)

@csrf_exempt
def update_inventory(request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        p = Product.objects.get(id=id)
        p.stock = data.get('stock', p.stock)
        p.price = data.get('price', p.price)
        p.save()
        return JsonResponse({'success': True})
    elif request.method == 'DELETE':
        Product.objects.filter(id=id).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'})
