from django.contrib.auth import views as auth_views
from django.urls import path

from .views import BlacklistTokenUpdateView, ManageUserView, RegisterView

app_name = 'account'

urlpatterns = [
       path('register-user/', RegisterView.as_view(), name="create_user"),
       path('fetch-user/', ManageUserView.as_view(), name="get_user"),
       path('change-password/', auth_views.PasswordChangeView.as_view()),
       path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
       path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
       path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
       path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
       path('update-user/', ManageUserView.as_view(), name="update_user"),
#        #  # Forget Password
#        path('password-reset/',
#          auth_views.PasswordResetView.as_view(
#              template_name='common/password-reset/password_reset.html',
#              subject_template_name='common/password-reset/password_reset_subject.txt',
#              email_template_name='common/password-reset/password_reset_email.html',
#              # success_url='/login/'
#          ),
#          name='password_reset'),
#        path('password-reset/done/',
#          auth_views.PasswordResetDoneView.as_view(
#              template_name='common/password-reset/password_reset_done.html'
#          ),
#          name='password_reset_done'),
#        path('password-reset-confirm/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(
#              template_name='common/password-reset/password_reset_confirm.html'
#          ),
#          name='password_reset_confirm'),
#        path('password-reset-complete/',
#          auth_views.PasswordResetCompleteView.as_view(
#              template_name='common/password-reset/password_reset_complete.html'
#          ),
#          name='password_reset_complete'),
#
#        # path('update-user/', ManageUserView.as_view(), name="update_user"),

]