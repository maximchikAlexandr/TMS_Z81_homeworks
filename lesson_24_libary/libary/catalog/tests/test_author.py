from django.test import TestCase

from catalog.models import Author


class AuthorTest(TestCase):
    fixtures = ["catalog/tests/fixtures/author_fixture.json"]

    def test_str_representation(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.pseudonym, str(author))
