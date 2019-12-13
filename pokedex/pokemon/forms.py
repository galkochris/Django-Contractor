from django import forms
from pokemon.models import Pokemon


class PokemonForm(forms.ModelForm):
    """ Render and process a form based on the Pokemon model. """
    model = Pokemon