from django.test import TestCase

# Create your tests here.
class AccountTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)


from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class ViewTestCase(TestCase):
    def test_login(self):
        """Tests if a user can sign up"""
        Username = request.POST["Joe"]
        Password = request.POST["WootWoot"]
        self.assertEqual("Joe", Username)
        self.assertEqual("WootWoot", Password)