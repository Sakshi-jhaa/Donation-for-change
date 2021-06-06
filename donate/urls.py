from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', include('donation.urls')),
    path('admin/', admin.site.urls),

    
]
