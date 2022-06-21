
from rest_framework import serializers


#-------회원가입(사용자 등록) --------
from rest_framework_simplejwt.tokens import RefreshToken

from accountapp.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["email","username","password","gender","date_joined"]

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user


#-----------로그인 ------------
class JWTLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100,write_only=True, style={"input_type": "password"})
    # access = serializers.CharField(read_only=True)
    # refresh = serializers.CharField(read_only=True)
    # role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["email","password"]
#
    def create(self, validate_date):
        pass

    def update(self,instance,validate_data):
        pass

    def validate(self,data):
        email = data["email"]
        password = data["password"]
        # user = authenticate(email=email, password=password)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError("wrong password")

        else:
            raise serializers.ValidationError("user account is not exist")

        token = RefreshToken.for_user(user=user)
        data = {
            "user" : user.email,
            "refresh_token" : str(token),
            "access_token" : str(token.access_token)
        }

        return data

