from django.test import TestCase, Client
from .models import Item
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_object_created(self):
        item = Item.objects.create(name = 'Ellisha Natasha', amount = 70, description = 'Book')
        self.assertEquals(item.name, 'Ellisha Natasha')
        