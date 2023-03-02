from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_code>/', views.redirect_original, name='redirect_original'),
    path('<str:short_code>/stats/', views.short_url_created, name='short_url_created'),
    path('shorten/', views.generate_short_code, name='shorten_url'),
]
