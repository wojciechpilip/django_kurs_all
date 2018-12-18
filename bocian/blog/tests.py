from django.test import TestCase

# Create your tests here.
from blog.models import Wpis


class TestBlogRoutes(TestCase):
    fixtures = ['blog']
    def test_main_page_of_blog_exists(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_czy_mozna_obejrzec_dowolny_wpis(self):
        response = self.client.get('/blog/wpisy/2')
        self.assertContains(response, '<h1>Drugi wpis</h1>')
        self.assertContains(response, '<div class="tresc_wpisu">Zabawa była przednia</div>')


class TestWpisModel(TestCase):

    def test_can_create_wpis(self):
        w = Wpis(
            tytul="Ala ma kota",
            tresc="Kot ma Alę"

        )
        w.save()
        self.assertEqual(w, Wpis.objects.last())
        w.delete()
