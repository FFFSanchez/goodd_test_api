from django.urls import path, include

from .views import UserViewSet, RegisterView, LogoutAllView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter


app_name = 'users'


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    #path('v1/user/', UserRetrieveUpdateAPIView.as_view()),
    path('v1/register/', RegisterView.as_view(), name='auth_register'),
    path('v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/logout/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('v1/', include(router.urls)),
]
