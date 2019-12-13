from django.urls import path
from pokemon.views import PokemonListView, PokemonDetailView, PokemonCreateView


urlpatterns = [
    path('', PokemonListView.as_view(), name='pokemon-list-page'),
    path('create/', PokemonCreateView.as_view(), name='pokemon-create-page'),
    path('<str:slug>/', PokemonDetailView.as_view(), name='pokemon-details-page'),
]