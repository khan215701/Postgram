from rest_framework.response import Response
from rest_framework import viewsets
from core.auth.serializers.registerserializer import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import HTTP_201_CREATED



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