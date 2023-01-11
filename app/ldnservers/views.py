"""
views for ldnsql server APIs
"""
from django.http import Http404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SQLServer
from .serializers import SQLServerSerializer


class CreateSQLServer(CreateAPIView):
    serializer_class = SQLServerSerializer


class SQLServers(ListAPIView):
     permission_classes = [IsAuthenticated]
     queryset = SQLServer.objects.all()
     serializer_class = SQLServerSerializer


@extend_schema(
    parameters=[
        OpenApiParameter(name='server_id',location=OpenApiParameter.QUERY, description='server_id', required=True, type=str),
    ],
)
class SQLServerView(GenericAPIView):
    """
    """

    serializer_class = SQLServerSerializer
    queryset = SQLServer.objects.all()

    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = SQLServer.objects.all()
        return users

    def get(self, request):

        try:
            server_id = self.request.query_params.get('server_id',None)

            if server_id != None:
                queryset = self.get_queryset().filter(server_id=server_id)
                serializer = SQLServerSerializer(queryset,many=True)
                return Response(serializer.data)
        except:
            user = self.get_queryset()
            serializer = SQLServerSerializer(user)
        return Response({})



"""
update server view
"""
class SQLServerUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SQLServerSerializer

    """
    Retrieve, update or delete a transformer instance
    """
    def get_object(self, pk):

        # Returns an object instance that should
        # be used for detail views.
        try:
            return SQLServer.objects.get(pk=pk)
        except SQLServer.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        server = self.get_object(pk)
        serializer = SQLServerSerializer(server, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        server = self.get_object(pk)
        serializer = SQLServerSerializer(server,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,pk):
        server = self.get_object(pk)
        server.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

