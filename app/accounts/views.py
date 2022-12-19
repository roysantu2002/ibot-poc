from rest_framework import permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase

from .serializers import (CustomUserSerializer, MyTokenObtainPairSerializer,
                          TokenObtainLifetimeSerializer,
                          TokenRefreshLifetimeSerializer)

"""
    RegisterView
"""
class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )
    # permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    # json = serializer.data
                    return Response({'code' : 'account-created'}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error' : 'something-went-wrong-while-saving'},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                )
            else:
                default_errors = serializer.errors
                new_error = {}
                for field_name, field_errors in default_errors.items():
                    new_error[field_name] = field_errors[0]

                return Response({'error' :new_error}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:

            return Response(
                {'error' : 'validation error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
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

"""
UserView
"""

class UserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = CustomUserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )