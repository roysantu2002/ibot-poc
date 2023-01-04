"""
URL's for ldnsql app
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CreateSQLUser, SQLUserList, SQLUserView

# router = DefaultRouter()
# router.register('ldnsql', views.SQLUserView)

app_name = 'ldnsql'

urlpatterns = [
       path('sqlusers/', SQLUserView.as_view(), name="sql_user"),
       path('createsqluser/', CreateSQLUser.as_view(), name="create_sql_user"),
       path('sqluserlist/{user_id}', SQLUserList.as_view(), name="sql_user_list"),


]

# urlpatterns = [
#    url('ldnsql', SQLUserView.as_view())
# ]