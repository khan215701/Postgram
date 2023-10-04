from django.urls import path, include
from rest_framework import routers
from core.user.views import UserViewSet
from core.auth.viewset.register import RegisterViewSet
from core.auth.viewset.login import LoginViewSet
from core.auth.viewset.refresh import RefreshViewSet

router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='register_user')
router.register(r'auth/login', LoginViewSet, basename='login')
router.register(r'auth/refresh', RefreshViewSet, basename='refresh')


urlpatterns = [
    path('api/', include(router.urls)),
]

