from django.contrib import admin
from django.urls import include, path
from scores.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("scores.urls")),
    path("", home, name="home"),
]
