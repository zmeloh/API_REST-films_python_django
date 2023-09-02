from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from film_api import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Film API",
        default_version='v1',
        description="API pour gérer les films, les favoris et les utilisateurs.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Définissez un routeur pour vos vues DRF
router = routers.DefaultRouter()
router.register(r'films', views.FilmViewSet)
router.register(r'favorites', views.FavoriteViewSet)
router.register(r'users', views.UserProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour l'interface d'administration Django
    path('api/', include(router.urls)),  # URL pour les vues DRF
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
