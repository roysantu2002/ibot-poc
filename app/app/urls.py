"""
"""

from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include('api.urls', namespace='api')),
    path('api/account/', include('account.urls')),
    path('api/sql-user/', include('sqluser.urls')),
    path('api/sql-server/', include('sql.urls')),
    path('api/account/login/', TokenObtainPairView.as_view()),
    path('api/account/token/refresh/', TokenRefreshView.as_view()),
    path('api/account/token/verify/', TokenVerifyView.as_view()),
    # path('api/account/', include('api.urls')),


]