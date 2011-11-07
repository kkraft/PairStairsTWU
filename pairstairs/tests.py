"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client, RequestFactory
from models import Programmer, Pair
from views import add_count, delete_programmers, delete_programmer, reset_counts


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

    def test_add_count_adds_1_to_pair_count(self):
        factory = RequestFactory()
        request = factory.get('request')
        programmer1 = Programmer(name='Kory Kraft')
        programmer1.save()
        programmer2 = Programmer(name='Jason Wickstra')
        programmer2.save()
        pair = Pair(pair1=programmer1, pair2=programmer2, count=0)
        pair.save()
        add_count(request=request, pair1_id=1, pair2_id=2)
        pair = Pair.objects.get(pk=1)
        self.assertEqual(pair.count, 1)

    def test_that_all_programmers_get_deleted(self):
        factory = RequestFactory()
        request = factory.get('request')
        programmer1 = Programmer(name='Kory Kraft')
        programmer1.save()
        programmer2 = Programmer(name='Jason Wickstra')
        programmer2.save()
        delete_programmers(request)
        self.assertEqual(0,len(Programmer.objects.all()))

    def test_selected_programmer_gets_deleted(self):
        factory = RequestFactory()
        request = factory.get('request')
        programmer1 = Programmer(name='Kory Kraft')
        programmer1.save()
        programmer2 = Programmer(name='Jason Wickstra')
        programmer2.save()
        delete_programmer(request,1)
        self.assertEqual(1,len(Programmer.objects.all()))
        self.assertEqual('Jason Wickstra', Programmer.objects.all()[0].name)

    def test_reset_changes_pair_counts_to_zero(self):
        factory = RequestFactory()
        request = factory.get('request')
        programmer1 = Programmer(name='Kory Kraft')
        programmer1.save()
        programmer2 = Programmer(name='Jason Wickstra')
        programmer2.save()
        pair = Pair(pair1=programmer1, pair2=programmer2, count=0)
        pair.save()
        add_count(request=request, pair1_id=1, pair2_id=2)
        add_count(request=request, pair1_id=1, pair2_id=2)
        pair = Pair.objects.get(pk=1)
        self.assertEqual(pair.count, 2)
        reset_counts(request)
        pair = Pair.objects.get(pk=1)
        self.assertEqual(pair.count, 0)
        






