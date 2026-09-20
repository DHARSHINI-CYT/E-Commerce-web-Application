import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Product

def seed():
    Product.objects.all().delete()
    
    products = [
        {
            'name': 'Sony WH-1000XM4',
            'description': 'Noise Cancelling Headphones',
            'price': 348.00,
            'original_price': None,
            'sku': 'ELC-SNY-001',
            'stock': 42,
            'image_url': 'https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?auto=format&fit=crop&q=80&w=800',
            'badge': 'NEW'
        },
        {
            'name': 'Apple Watch Series 8',
            'description': 'Smartwatch with Midnight Band',
            'price': 399.00,
            'original_price': None,
            'sku': 'ELC-APL-W8',
            'stock': 3,
            'image_url': 'https://images.unsplash.com/photo-1579586337278-3befd40fd17a?auto=format&fit=crop&q=80&w=800',
            'badge': None
        },
        {
            'name': 'Polaroid OneStep+',
            'description': 'Instant Camera',
            'price': 119.99,
            'original_price': 149.99,
            'sku': 'CAM-PLR-01',
            'stock': 0,
            'image_url': 'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&q=80&w=800',
            'badge': 'SALE -20%'
        },
        {
            'name': 'Apple Watch SE',
            'description': 'Starlight Aluminum Case',
            'price': 249.00,
            'original_price': None,
            'sku': 'ELC-APL-SE',
            'stock': 15,
            'image_url': 'https://images.unsplash.com/photo-1434494878577-86c23bcb06b9?auto=format&fit=crop&q=80&w=800',
            'badge': None
        },
        {
            'name': 'DJI Mini 3 Pro',
            'description': 'Lightweight Drone with 4K Video',
            'price': 759.00,
            'original_price': None,
            'sku': 'ELC-DJI-M3P',
            'stock': 10,
            'image_url': 'https://images.unsplash.com/photo-1473968512647-3e447244af8f?auto=format&fit=crop&q=80&w=800',
            'badge': 'HOT'
        },
        {
            'name': 'Marshall Stanmore II',
            'description': 'Wireless Bluetooth Speaker',
            'price': 349.99,
            'original_price': 399.99,
            'sku': 'ELC-MSH-S2',
            'stock': 25,
            'image_url': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&q=80&w=800',
            'badge': 'SALE -12%'
        },
        {
            'name': 'Logitech MX Master 3S',
            'description': 'Advanced Wireless Mouse',
            'price': 99.99,
            'original_price': None,
            'sku': 'ELC-LOG-MX3',
            'stock': 50,
            'image_url': 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&q=80&w=800',
            'badge': None
        },
        {
            'name': 'Nintendo Switch OLED',
            'description': 'Gaming Console - White Joy-Con',
            'price': 349.99,
            'original_price': None,
            'sku': 'GAM-NIN-OLED',
            'stock': 5,
            'image_url': 'https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?auto=format&fit=crop&q=80&w=800',
            'badge': 'RESTOCKED'
        }
    ]
    
    for p in products:
        Product.objects.create(**p)
    print("Done! Products seeded with fixed images.")

seed()
