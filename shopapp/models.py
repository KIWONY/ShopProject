from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="products", null= True)
    image = models.ImageField(upload_to="product/", null = False)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    available_order =models.BooleanField("Order",default=True)

    creted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('shopapp:product_detail',args=[self.id])




