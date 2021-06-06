from . import views
from django.urls import path


urlpatterns = [

    path('', views.bookstore, name='bookstore'),
    path('donate', views.donate, name='donate'),
    
]