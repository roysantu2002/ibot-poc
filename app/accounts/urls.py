from django.urls import path

from .views import BlacklistTokenUpdateView, RegisterView, ManageUserView

app_name = 'accounts'

urlpatterns = [
       path('register/', RegisterView.as_view(), name="create_user"),
       path('user/', ManageUserView.as_view(), name="get_user"),
       # path('update-user/', ManageUserView.as_view(), name="update_user"),

]