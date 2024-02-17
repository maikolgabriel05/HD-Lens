from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dashboard/', include('pages.urls')),
    path('dashboard/customer/', include('customers.urls')),
    path('dashboard/products/', include('products.urls')),
    path('shopping/', include('shopping.urls', namespace='shopping')),
    path('api/products/', v.api_product, name='api_product'),
    path('api/shopping-items/add/', v.api_shopping_items_add, name='api_shopping_items_add'),
    path('api/v1/', include('api.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns += staticfiles_urlpatterns()
