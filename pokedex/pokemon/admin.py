from django.contrib import admin
from pokemon.models import Pokemon


class PokemonAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('name', 'slug', 'entry', 'created', 'modified')


admin.site.register(Pokemon, PokemonAdmin)