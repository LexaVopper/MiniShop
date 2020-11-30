from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prod/', include('product.urls')),
    path('api/', include('api.urls')),
    path('account/', include('account.urls')),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
