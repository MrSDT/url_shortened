from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('<short_code>/', views.redirect_original, name='redirect_original'),
    path('<short_code>/stats/', views.shorten_url_created, name='shorten_url_created'),
]
