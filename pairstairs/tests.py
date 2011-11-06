"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from models import Programmer, Pair


class PairStairsTests(TestCase):
    def test_that_create_stairs_page_renders(self):
        response = Client().get('/add_programmer/')
        self.assertEquals(response.status_code, 200)

    def test_that_create_stairs_template_exists(self):
        response = Client().get('/add_programmer/')
        self.assertTemplateUsed(response, 'add_programmer.html')

    def test_should_add_programmer_name_to_list_after_submitted(self):
        response = Client().post('/add_programmer/', {'programmer_names': 'Kory Kraft'})
        self.assertContains(response, 'Kory Kraft')

    def test_should_save_programmers(self):
        Client().post('/add_programmer/', {'programmer_names': 'Kory Kraft'})
        self.assertTrue(Programmer.objects.filter(name='Kory Kraft'))

    def test_that_create_stairs_page_renders(self):
        response = Client().get('/pairstairs/')
        self.assertEquals(response.status_code, 200)

    def test_that_pair_stairs_template_exists(self):
        response = Client().get('/pairstairs/')
        self.assertTemplateUsed(response, 'pairstairs.html')

    def test_that_pairs_get_saved(self):
        Client().post('/add_programmer/', {'programmer_names': 'Kory Kraft'})
        Client().post('/add_programmer/', {'programmer_names': 'Jason Wickstra'})
        pairs = Pair.objects.all()
        pair1_name = pairs[0].pair1.name
        pair2_name = pairs[0].pair2.name
        self.assertEqual(pair1_name, 'Kory Kraft')
        self.assertEqual(pair2_name, 'Jason Wickstra')
        self.assertEqual(pairs[0].count, 0)




