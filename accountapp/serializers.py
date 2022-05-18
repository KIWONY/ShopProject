from django.contrib.auth import authenticate
from django.contrib.auth.models import User, update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

#-------회원가입(사용자 등록) --------
class JWTSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["username","email","password","date_joined"]

    def create(self,validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


#-----------로그인 ------------
class JWTLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100,write_only=True, style={"input_type": "password"})
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["email","password"]

    def create(self, validate_date):
        pass

    def update(self,instance,validate_data):
        pass

    def validate(self,data):
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email, password=password)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError("wrong password")

        else:
            raise serializers.ValidationError("user account is not exist")


        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        update_last_login(None, user)

        validation = {
            "access" : access_token,
            "refresh" : refresh_token,
            "email" : user.email
        }

        return validation

