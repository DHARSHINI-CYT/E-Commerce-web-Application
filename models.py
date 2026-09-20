from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sku = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=500)
    badge = models.CharField(max_length=50, blank=True, null=True)

    def to_dict(self):
        status = 'In Stock' if self.stock > 10 else ('Low Stock' if self.stock > 0 else 'Out of Stock')
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': float(self.price),
            'original_price': float(self.original_price) if self.original_price else None,
            'sku': self.sku,
            'stock': self.stock,
            'image_url': self.image_url,
            'badge': self.badge,
            'status': status
        }
