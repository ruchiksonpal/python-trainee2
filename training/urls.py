"""training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# urlpatterns = [
#                   path('admin/', include('web.users.urls'), name='admin_login'),
#                   path('', RedirectView.as_view(url='admin/', permanent=False)),
#               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
import web

urlpatterns = [

                  path('admin/', include('web.users.urls'), name='admin_login'),
                  path('admin/', include('web.film.urls'), name='film_details'),
                  path('', RedirectView.as_view(url='admin/', permanent=False)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)