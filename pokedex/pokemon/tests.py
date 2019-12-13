from django.test import TestCase

class AccountTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)


from django.contrib.auth.models import User
from django.test import TestCase

from pokemon.models import Pokemon


class PokemonTesting(TestCase):
    def test_pokemon(self):
        # Make some test data to be displayed on the page.

        pokemon = Pokemon.objects.create(name="Grookey", entry="test", move="test")

        # Check that the response is 200 OK.
        self.assertEqual(pokemon.name, "Grookey")
        self.assertEqual(pokemon.entry, "test")