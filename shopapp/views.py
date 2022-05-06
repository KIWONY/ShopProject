from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from shopapp.forms import ProductCreationForm
from shopapp.models import Product


def main(request):
    return render(request,"shopapp/main.html")









