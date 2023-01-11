"""
URL's for ldnservers app
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (CreateSQLServer, SQLServers, SQLServerUpdateView,
                    SQLServerView)

# router = DefaultRouter()
# router.register('ldnsql', views.SQLUserView)

app_name = 'ldnservers'

urlpatterns = [
       path('sqlserver/', SQLServerView.as_view(), name="sql_user"),
       path('createsqlserver/', CreateSQLServer.as_view(), name="create_sql_user"),
       path('sqlserverlist/', SQLServers.as_view(), name="sql_user_list"),
       path('sqlserverupdate/<int:pk>', SQLServerUpdateView.as_view(), name="sql_server_udate"),


]