"""
URL's for ldnservers app
"""

from django.urls import path
# from rest_framework.routers import DefaultRouter

from .views import (CreateSQLServer, SQLServers, SQLServerUpdateView,
                    SQLServerView)

# router = DefaultRouter()
# router.register('ldnsql', views.SQLUserView)

app_name = 'sql-servers'

urlpatterns = [
       path('fetch-server/', SQLServerView.as_view(), name="fetch-server"),
       path('add-server/', CreateSQLServer.as_view(), name="add-server"),
       path('server-list/', SQLServers.as_view(), name="server-list"),
       path('manage-server/<int:pk>', SQLServerUpdateView.as_view(), name="manage-server"),
]