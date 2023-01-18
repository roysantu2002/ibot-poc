"""
views for ldnsql APIs
"""
from django.http import Http404
from django.views.generic.edit import UpdateView
from drf_spectacular.utils import (OpenApiParameter, OpenApiTypes,
                                   extend_schema, extend_schema_view)
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     ListAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sql.models import SQLServer
from sql.serializers import SQLServerSerializer

from .models import SQLUser
from .serializers import SQLUserSerializer, UpdateUserSerializer


class CreateSQLUser(CreateAPIView):
    serializer_class = SQLUserSerializer

class CustomerViewSet(UpdateAPIView):
    serializer_class = UpdateUserSerializer

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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = SQLUser.objects.all()
        return users

    def get_server(self, user_id):
        user_object = {}
        server_list = []
        server_id = self.get_queryset().filter(user_id=user_id).filter(flag=True).values('server')
        user_object['user_id'] = user_id

        for server in server_id:
            server_list.append(server['server'])

        for id in server_list:
            server_name = SQLServer.objects.filter(id=id).only("server_id").values('server_id')
            for name in server_name:
                user_object[id] = name
        return user_object

    def get(self, request):

        try:
            user_id = request.query_params.get('user_id',None)
            if user_id != None:
                user_obj = self.get_server(user_id)
                return Response(user_obj)

        except:
           return Response({'user_id': user_id})
        return Response({'user_id': user_id})

"""
update user view
"""
@extend_schema(
    parameters=[
        OpenApiParameter(name='user_id',location=OpenApiParameter.QUERY, description='user_id', required=False, type=str),
    ],
)

class SQLUserUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SQLUserSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            if SQLUser.objects.filter(user_id=user_id).exists():
                queryset = SQLUser.objects.filter(user_id=user_id)
                return queryset

    def delete(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            if queryset is not None:
                queryset.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:

            return Response(status=status.HTTP_400_BAD_REQUEST)
