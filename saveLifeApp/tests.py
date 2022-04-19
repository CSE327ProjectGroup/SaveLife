from django.test import TestCase
from views import result
from views import keyword
"""
to test if the user input keyword matching with the result data
"""
class TestViews(TestCase):
    def test_search(self):
        assert keyword == result

