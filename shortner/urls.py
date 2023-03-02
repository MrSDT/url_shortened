from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.generate_short_code, name='shorten_url'),
    path('<str:short_code>/', views.redirect_original, name='redirect_original'),
    path('stats/<str:short_code>/', views.short_url_created, name='url_stats'),
]
