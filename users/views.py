from rest_framework import status, viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import OwnerOrReadOnly
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, OwnerOrReadOnly]
