from django.urls import path, include
from django.views.generic import TemplateView

from shopapp import views

app_name = "shopapp"

urlpatterns = [
    path("", views.main),
]