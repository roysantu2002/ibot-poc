

from rest_framework import authentication, generics, permissions, status
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase

from .serializers import (CustomUserSerializer, MyTokenObtainPairSerializer,
                          TokenObtainLifetimeSerializer,
                          TokenRefreshLifetimeSerializer)



"""
    RegisterView
"""
class RegisterView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    # permission_classes = (permissions.AllowAny)
    permission_classes = [AllowAny]
#
#     def post(self, request):
#     try:
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 # json = serializer.data
#                 return Response({'code' : 'account-created'}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'error' : 'something-went-wrong-while-saving'},
#                                     status=status.HTTP_500_INTERNAL_SERVER_ERROR
#                                 )
#         else:
#             default_errors = serializer.errors
#             new_error = {}
#             for field_name, field_errors in default_errors.items():
#                 new_error[field_name] = field_errors[0]
#
#             return Response({'error' :new_error}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#
#         return Response(
#             {'error' : 'validation error'},
#             status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )

class BlacklistTokenUpdateView(APIView):
    # permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class TokenObtainPairView(TokenViewBase):
    """
        Return JWT tokens (access and refresh) for specific user based on username and password.
    """

    serializer_class = TokenObtainLifetimeSerializer


class TokenRefreshView(TokenViewBase):
    """
        Renew tokens (access and refresh) with new expire time based on specific user's access token.
    """
    serializer_class = TokenRefreshLifetimeSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

"""
UserView
"""

# class UserView(APIView):
#     serializer_class = CustomUserSerializer
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_object(self):
#         """Retrieve and return the authenticated user."""
#         return self.request.user

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""

    serializer_class = CustomUserSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [authentication.TokenAuthentication,]
    # permission_classes = [IsAuthenticated]

    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user

    # def get(self, request, format=None):
    #     content = {
    #         'user': str(request.user.email)
    #     }
    #     return Response(content)

    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    # print(permission_classes)

    # def get_object(self):
    #     print(self.request.user)
    #     """Retrieve and return the authenticated user."""
    #     return self.request.user
