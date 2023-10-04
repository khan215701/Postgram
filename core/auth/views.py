from rest_framework.response import Response
from rest_framework import viewsets
from .serializers.registerserializer import RegisterSerializer
from .serializers.loginserializer import LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
# Create your views here.

class RegisterViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token),
        }
        
        return Response({
            "user" : serializer.data,
            "refresh" : res['refresh'],
            "access" : res['access'] 
        }, status=HTTP_201_CREATED )
        

class LoginViewSet(viewsets.ViewSet):
    http_method_names = ('post',)
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data,
                        status=HTTP_200_OK)
            
            

class RefreshViewSet(viewsets.ViewSet):
    http_method_names = ('post',)
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=HTTP_200_OK)
