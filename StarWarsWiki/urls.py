"""StarWarsWiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path

from .views import index, contact, characters, fake_request_view, films, planets, species, starships_vehicles
from StarWarsWiki import settings

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"), 
    path('films/', films, name="films"),
    path('characters/', characters, name="characters"),
    path('planets/', planets, name="planets"),
    path('species/', species, name="species"),
    path('starships_vehicles/', starships_vehicles, name="starships_vehicles"),
    path('404/', fake_request_view, name='fake-request'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
