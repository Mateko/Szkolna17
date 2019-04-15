from django.urls import path

from . import views

app_name = 'teleturniej'
urlpatterns = [
    path('', views.get_name, name='index'),
    path('game', views.game, name='game'),
    path('level_result', views.level_result, name='level_result'),
    path('life_preserver/', views.life_preserver, name='life_preserver'),
]

