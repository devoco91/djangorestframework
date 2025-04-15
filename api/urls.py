from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def root_view(request):
    return Response({"message": "✅ Weekday API root is working!"})

schema_view = get_schema_view(
   openapi.Info(
      title="Weekday API",
      default_version='v1',
      description="API documentation for Contact, Products, Applicants",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="support@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/', include('registration.urls')),
    path('api/', include('contact.urls')),
    path('api/', include('products.urls')),
    # path('api/', include('applicants.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
