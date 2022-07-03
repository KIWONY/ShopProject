from django.urls import path


from . import views
from .views import JWTLoginView, SignUpView

app_name = "accountapp"

urlpatterns = [
    path('accounts',SignUpView.as_view()),
    path('login' , JWTLoginView.as_view(), name="login")

]