from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('<str:short_code>/', views.redirect_original, name='redirect_original'),
    path('<str:short_code>/stats/', views.short_url_created, name='short_url_created'),
]
