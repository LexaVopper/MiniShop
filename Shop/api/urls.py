from django.contrib import admin
from django.urls import include, path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'api'
urlpatterns = [
    path('product/', views.add_product, name='add_product'),
    path('update_session/', views.update_session, name='update_session'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('complete_cart/', views.complete_cart, name='complete_cart'),
    #path('product/<int:pk>', views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)