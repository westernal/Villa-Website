from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from User.serializers import UserInfoSerializer, UserSerializer, UserTokenSerializer \
                           , UserUpdateSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.


# Creates a user
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()


# User Login
class UserTokenView(TokenObtainPairView):
    serializer_class = UserTokenSerializer

    
# Updating user information
class ManageUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user


# Retrieving authenticated user's information
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        uID = getattr(self.request.user,'userID')
        return get_user_model().objects.filter(userID=uID)

    def get_object(self):
        uID = getattr(self.request.user,'userID')
        return self.queryset.filter(userID=uID)





