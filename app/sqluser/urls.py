"""
URL's for ldnsql app
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (CreateSQLUser, CustomerViewSet, SQLUserList,
                    SQLUserUpdateView, SQLUserView)

# router = DefaultRouter()
# router.register('ldnsql', views.SQLUserView)

app_name = 'sql-users'

urlpatterns = [
       path('fetch-user/', SQLUserView.as_view(), name="fetch-user"),
       path('add-user/', CreateSQLUser.as_view(), name="add-user"),
       path('user-list/', SQLUserList.as_view(), name="user-list"),
       path('manage-user/<int:pk>', SQLUserUpdateView.as_view(), name="manage-user"),



]

# urlpatterns = [
#    url('ldnsql', SQLUserView.as_view())
# ]