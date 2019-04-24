from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'teleturniej'

urlpatterns = [
    path('', views.get_name, name='index'),
    path('game', views.game, name='game'),
    path('level_result', views.level_result, name='level_result'),
    path('life_preserver/', views.life_preserver, name='life_preserver'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)