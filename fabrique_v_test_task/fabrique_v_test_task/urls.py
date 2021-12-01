from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(title="Fabrique V Test Task API", default_version="v1", description="API для приложения-опросника"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    # Swagger url
    path("swagger/", schema_view.with_ui(cache_timeout=0), name="schema-swagger-ui"),
]
