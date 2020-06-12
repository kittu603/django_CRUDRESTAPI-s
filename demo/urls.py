from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store import api_views

import store.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/<int:id>/', store.views.show, name='show-product'),
    path('cart/', store.views.cart, name='shopping-cart'),
    path('', store.views.index, name='list-products'),
    path('api/products', api_views.ProductListApiView.as_view(), name = 'products-list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
