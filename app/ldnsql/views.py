"""
views for ldnsql APIs
"""
from drf_spectacular.utils import (OpenApiParameter, OpenApiTypes,
                                   extend_schema, extend_schema_view)
from ldnsql.models import SQLUser
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SQLUserSerializer


class CreateSQLUser(CreateAPIView):
    serializer_class = SQLUserSerializer


class SQLUserList(ListAPIView):
     permission_classes = [IsAuthenticated]
     queryset = SQLUser.objects.all()
     serializer_class = SQLUserSerializer


@extend_schema(
    parameters=[
        OpenApiParameter(name='user_id',location=OpenApiParameter.QUERY, description='user_id', required=False, type=str),
    ],
)
class SQLUserView(GenericAPIView):
    """
    """

    serializer_class = SQLUserSerializer
    queryset = SQLUser.objects.all()

    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = SQLUser.objects.all()
        return users

    def get(self, request):

        try:
            user_id = self.request.query_params.get('user_id',None)
            print(user_id)

            if user_id != None:
                queryset = self.get_queryset().filter(user_id=user_id)
                serializer = SQLUserSerializer(queryset,many=True)
                return Response(serializer.data)
        except:
            user = self.get_queryset()
            serializer = SQLUserSerializer(user)
        return Response({})

