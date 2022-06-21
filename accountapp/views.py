
# Create your views here.
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

#
# https://hayeon1549.tistory.com/36
# https://breathtaking-life.tistory.com/137?category=835829
# https://ssilook.tistory.com/entry/%EC%9E%A5%EA%B3%A0%EC%99%80-%EB%A6%AC%EC%95%A1%ED%8A%B8Django-React%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0-3-Django-App-%EC%83%9D%EC%84%B1?category=876974
# https://velog.io/@ssssujini99/DjangoWeb-Django%EC%9D%98-simple-jwt%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B8%B0%EB%8A%A5-%EA%B5%AC%ED%98%841


# https://www.django-rest-framework.org/api-guide/views/#class-based-views
from rest_framework_simplejwt.tokens import RefreshToken

from accountapp.serializers import UserCreateSerializer, JWTLoginSerializer


# -----------회원가입---------------
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def signup(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data,status=201)



# #---------------로그인-------------
class JWTLoginView(generics.GenericAPIView):
    serializer_class = JWTLoginSerializer
    permission_classes = ((AllowAny,))

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token":token},status=status.HTTP_200_OK)

