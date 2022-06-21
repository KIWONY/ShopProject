from django.urls import path


from . import views
from .views import JWTLoginView

app_name = "accountapp"

urlpatterns = [
    path('accounts',views.signup),
    path('login' , JWTLoginView.as_view(), name="login")

]