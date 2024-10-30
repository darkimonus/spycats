from django.contrib import admin
from django.urls import path, include

from cats.urls import urlpatterns as cats_urls
from missions.urls import urlpatterns as missions_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cats/', include(cats_urls)),
    path('missions/', include(missions_urls)),
]
