"""
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include('api.urls', namespace='api')),
    path('api/account/', include('accounts.urls')),
    # path('api/account/', include('api.urls')),


]