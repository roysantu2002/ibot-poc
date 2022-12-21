"""
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include('api.urls', namespace='api')),
    path('api/account/', include('accounts.urls')),
    path('api/token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    # path('api/account/', include('api.urls')),


]