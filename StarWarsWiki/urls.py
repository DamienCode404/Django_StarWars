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
from django.urls import path, re_path

from .views import index, characters, error_404, films, planets, species, starships_vehicles, character_details
from StarWarsWiki import settings

urlpatterns = [
    path('', index, name="index"),
    path('films/', films, name="films"),
    path('characters/', characters, name="characters"),
    path('planets/', planets, name="planets"),
    path('species/', species, name="species"),
    path('starships_vehicles/', starships_vehicles, name="starships_vehicles"),
    re_path(r'^id/(?P<character_id>[1-9]|[1-7][0-9]|[8][0-8])/$', character_details, name='character_details'),
    # La route par défaut pour la page 404
    re_path(r'^.*/$', error_404),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

