from django.contrib import admin

# Register your models here.
from accountapp.models import Comment

admin.site.register(Comment)