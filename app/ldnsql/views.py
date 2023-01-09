"""
views for ldnsql APIs
"""
from drf_spectacular.utils import (OpenApiParameter, OpenApiTypes,
                                   extend_schema, extend_schema_view)
from ldnservers.models import SQLServer
from ldnservers.serializers import SQLServerSerializer
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

    def get_server(self, user_id):
        user_object = {}
        server_list = []
        # server_id = self.get_queryset().filter(user_id=user_id).only("server")
        server_id = self.get_queryset().filter(user_id=user_id).only("server").values('server')

        for server in server_id:
            server_list.append(server['server'])
            # serializer = SQLUserSerializer(id_, many=True)
            # print(serializer.data)
            # print(id_)
        for id in server_list:
            server_name = SQLServer.objects.filter(id=id).only("server_id").values('server_id')
            for name in server_name:
                    print(name)
                    print(id, name)
                    user_object[id] = name
        user_object['user_id'] = user_id

            #   serializer = SQLServerSerializer(server_name, many=True)
        # return serializer.data

        # serializer = SQLUserSerializer(server_id, many=True)
        # print(serializer.data)
        # server_name = SQLServer.objects.filter(id=server_id)
        # serializer = SQLServerSerializer(server_name, many=True)

        return user_object

    def get(self, request):

        try:
            user_id = self.request.query_params.get('user_id',None)
            # server = self.get_server(user_id)
            # print(server)
            if user_id != None:
                queryset = self.get_queryset().filter(user_id=user_id)
                user_obj = self.get_server(user_id)
                # for user in queryset:
                #     # print(user)
                #     server = self.get_server(user)
                #     # print(server)
                # serializer = SQLUserSerializer(queryset, many=True)
                # return Response(serializer.data)
                return Response(user_obj)

        except:
            user = self.get_queryset()
            serializer = SQLUserSerializer(user)
        return Response({})

