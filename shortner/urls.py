from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_code>/', views.redirect_original, name='redirect_original'),
    path('<str:short_code>/stats/', views.short_url_created, name='short_url_created'),
    path('shorten/', views.index, name='shorten_url'),
]
