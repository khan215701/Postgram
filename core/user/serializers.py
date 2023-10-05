from core.abstract.serializers import AbstractSerlizer
from .models import User
class UserSerializer(AbstractSerlizer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                    'last_name', 'bio', 'avatar', 'email',
                    'is_active', 'created', 'updated']
        read_only = ['is_active']