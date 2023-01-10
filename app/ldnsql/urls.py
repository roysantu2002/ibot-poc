"""
URL's for ldnsql app
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (CreateSQLUser, CustomerViewSet, SQLUserList,
                    SQLUserUpdateView, SQLUserView)

# router = DefaultRouter()
# router.register('ldnsql', views.SQLUserView)

app_name = 'ldnsql'

urlpatterns = [
       path('sqluser/', SQLUserView.as_view(), name="sql_user"),
       path('createsqluser/', CreateSQLUser.as_view(), name="create_sql_user"),
       path('sqluserlist/', SQLUserList.as_view(), name="sql_user_list"),
       path('sqluserupdate/<int:pk>', SQLUserUpdateView.as_view(), name="sql_user_udate"),



]

# urlpatterns = [
#    url('ldnsql', SQLUserView.as_view())
# ]