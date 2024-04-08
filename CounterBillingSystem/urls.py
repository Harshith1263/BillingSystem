# urls.py (myproject)
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import get_schema_view
from drf_yasg import openapi

schema_view  = get_schema_view(
    openapi.Info(
        title = 'Counter Billing System API',
        default_version = 'v1',
        description = 'This is the API for the Billing System'
    ),
    public = True,
    pemission_classes=  (permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('api/',schema_view.with_ui('swagger', cache_timeout=0)),
]
