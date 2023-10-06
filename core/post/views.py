from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from core.abstract.viewset import AbstractViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import BasePermission, SAFE_METHODS
# Create your views here.


class PostViewSet(AbstractViewSet):
     http_method_names = ['post', 'get', 'put', 'delete']
     serializer_class = PostSerializer
     permission_classes = [IsAuthenticated]
     
     def get_queryset(self):
          return Post.objects.all()
      
     def get_object(self):
        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
     def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer. is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=HTTP_201_CREATED)
    
    
class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        
        if view.basename in ['post']:
            return bool(request.user and request.user.is_authenticated)

        return False
    
    def has_permission(self, request, view):
        if view.basename in ['post']:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            
            return bool(request.user and request.user.is_authenticated)
        
        return False
    
       