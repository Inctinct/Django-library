from django.test import TestCase
from ..models import Author


class FirstTest(TestCase):
    fixtures = ['catalog/tests/fixtures/fixture1.json']
    # @classmethod
    # def setUpTestData(cls):
    #     # Set up non-modified objects used by all test methods
    #     Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_example(self):
        author = Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))