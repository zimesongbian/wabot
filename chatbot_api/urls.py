from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('chatbot.urls')),  # Includes chatbot app's URLs under /api/
# ]


from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger schema view
schema_view = get_schema_view(
   openapi.Info(
      title="Chatbot API",
      default_version='v1',
      description="API for interacting with the chatbot",
      contact=openapi.Contact(email="admin@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chatbot.urls')),  # Include app-level URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
