from rest_framework.response import Response
from rest_framework import viewsets
from core.auth.serializers.loginserializer import LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

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
            