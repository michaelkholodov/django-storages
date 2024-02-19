from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from catalog.views import CategoryViews, TagViews, GoodsViews, HelloViews, \
    CategoryListViews, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

Router = routers.DefaultRouter()

Router.register('category', CategoryViews)
Router.register('goods', GoodsViews)


schema_view = get_schema_view(
    openapi.Info(
        title='Catalog API',
        default_version='v3',
        description='Catalog API',
    ),
    public=True,
    # permission_classes=(permission.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(Router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tags', TagViews.as_view({'get': 'list'})),
    path('api-auth/', include('rest_framework.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),

    path('', HelloViews.as_view(), name='hello'),
    path('category-list', CategoryListViews.as_view(), name='category-list'),
    path('category_detail/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category-create', CategoryCreateView.as_view(), name='category-create'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category_delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),

    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
