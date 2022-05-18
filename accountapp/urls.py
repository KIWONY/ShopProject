from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from accountapp.views import SignUpView, JWTLoginView

app_name = "accountapp"

urlpatterns = [
    # 토큰
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    # 로그인
    path('accounts', SignUpView.as_view(), name="signup"),
    path('login' , JWTLoginView.as_view(), name="login")

]