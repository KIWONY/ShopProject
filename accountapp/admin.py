from django.contrib import admin

# Register your models here.
from accountapp.models import User

admin.site.register(User)