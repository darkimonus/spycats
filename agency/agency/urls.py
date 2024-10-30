from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from cats.urls import urlpatterns as cats_urls
from missions.urls import urlpatterns as missions_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Cats Agency Api",
        default_version='v1',
        description="Agency description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cats/', include(cats_urls)),
    path('missions/', include(missions_urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
