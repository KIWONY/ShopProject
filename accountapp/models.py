from django.db import models

# Create your models here.

class Comment(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length= 50)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.email)