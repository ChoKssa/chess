from django.urls import path
from . import views

app_name = 'a_game'

urlpatterns = [
    path('new/', views.create_game, name='create_game'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
]
