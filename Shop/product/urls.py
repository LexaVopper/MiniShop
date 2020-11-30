from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'product'
urlpatterns = [
    path('product/<int:product_id>', views.product, name='product_single'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)