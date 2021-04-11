from django.urls import path
from tarea_app import views

urlpatterns = [
    path('', views.get_season, name = "get_season"),
    path('characters/<int:id>/',views.character_detail, name = "character_detail"),
    path('temporada/season/<int:season>', views.season_detail, name = "season_detail"),
    path('temporada/season2/<int:season>', views.season_detail2, name = "season_detail2"),
    path('episode/<int:id>', views.episode_detail, name = "episode_detail"),
    path(r'character_detail/', views.character),
    path('buscar/', views.search_characters, name="search_characters")

]