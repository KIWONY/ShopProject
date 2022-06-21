from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

app_name = "accountapp"

urlpatterns = [
    # 로그인
    path('accounts',views.signup),
    # path('login' , JWTLoginView.as_view(), name="login")

]