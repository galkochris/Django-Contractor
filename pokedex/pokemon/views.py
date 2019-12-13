from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from pokemon.models import Pokemon
from .forms import PokemonForm


class PokemonListView(ListView):
    """ Renders a list of all Pages. """
    model = Pokemon

    def get(self, request):
        """ GET a list of Pokemon. """
        pokemons = self.get_queryset().all()
        return render(request, 'list.html', {
          'pokemon': pokemons
        })

class PokemonDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Pokemon

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        pokemons = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'pokemon': pokemons
        })

class PokemonCreateView(CreateView):
    model = Pokemon
    fields = ['name', 'entry', 'moves']
    template_name = 'create_pokemon.html'
