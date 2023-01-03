"""
views for ldnsql APIs
"""

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


class SQLUserView(GenericAPIView):
    """
    """
    serializer_class = SQLUserSerializer
    queryset = SQLUser.objects.all()
    print(queryset)
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = SQLUser.objects.all()
        return users

    def get(self, request):

        try:
            id = request.query_params["id"]
            print(id)
            if id != None:
                user = SQLUser.objects.get(id=id)
                serializer = SQLUserSerializer(user)
        except:
            user = self.get_queryset()
            serializer = SQLUserSerializer(user)
        return Response(serializer.data)

