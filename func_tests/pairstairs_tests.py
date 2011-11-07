from django.utils.unittest.case import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from pairstairs.models import Programmer


class TestPairStairs(TestCase):

    def test_that_programmers_are_added_to_programmer_list_when_name_is_entered_and_submitted(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/add_programmer')
        self.assertEqual(self.driver.title, "Add Programmers")
        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_names')
        element.send_keys('Kory Kraft')
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmer').click()
        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_names')
        element.send_keys('Jason Wickstra')
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmer').click()
        programmer_elements = self.driver.find_elements(By.CSS_SELECTOR, '.name')
        self.assertEqual(2, len(programmer_elements))
        self.assertEqual('Kory Kraft', programmer_elements[0].text)
        self.assertEqual('Jason Wickstra', programmer_elements[1].text)


    def test_that_no_names_remain_in_programmer_list_when_delete_programmers_clicked(self):
        self.prepare_two_programmers()
        self.driver.find_element(By.CSS_SELECTOR, '#delete_programmers').click()
        self.assertEqual(0,len(self.driver.find_elements(By.CSS_SELECTOR, '.name')))


    def test_that_pair_stairs_are_created_after_create_pair_stairs_is_clicked(self):
        self.prepare_two_programmers()
        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_names')
        element.send_keys('James Grate')
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmer').click()
        self.driver.find_element(By.CSS_SELECTOR, '#pairstairs').click()
        self.assertEqual(self.driver.title, "Pair Stairs")
        programmer_elements = self.driver.find_elements(By.CSS_SELECTOR, '#programmer_row')
        self.assertEqual('Kory Kraft', programmer_elements[0].text)
        self.assertEqual('Jason Wickstra', programmer_elements[1].text)

    def test_that_clicking_on_pairing_count_adds_1(self):
        self.prepare_two_programmers()
        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_names')
        element.send_keys('James Grate')
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmer').click()
        self.driver.find_element(By.CSS_SELECTOR, '#pairstairs').click()
        self.assertEqual(self.driver.title, "Pair Stairs")
        self.driver.find_element(By.CSS_SELECTOR, '#pair_count').click()
        pair_count = self.driver.find_element(By.CSS_SELECTOR, '#pair_count')
        self.assertEqual(pair_count.text, '1')

    def test_that_link_back_to_add_programmers_works_correctly(self):
        self.prepare_two_programmers()
        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_names')
        element.send_keys('James Grate')
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmer').click()
        self.driver.find_element(By.CSS_SELECTOR, '#pairstairs').click()
        self.assertEqual(self.driver.title, "Pair Stairs")
        self.driver.find_element(By.CSS_SELECTOR, '#back_to_add_programmers').click()
        self.assertEqual(self.driver.title, "Add Programmers")

    def test_that_clicking_reset_counts_changes_counts_to_zero(self):
        self.prepare_two_programmers()
        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_names')
        element.send_keys('James Grate')
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmer').click()
        self.driver.find_element(By.CSS_SELECTOR, '#pairstairs').click()
        self.assertEqual(self.driver.title, "Pair Stairs")
        self.driver.find_element(By.CSS_SELECTOR, '#pair_count').click()
        self.driver.find_element(By.CSS_SELECTOR, '#reset_counts').click()
        pair_count = self.driver.find_element(By.CSS_SELECTOR, '#pair_count')
        self.assertEqual(pair_count.text, '0')

    def tearDown(self):
        Programmer.objects.all().delete()
        self.driver.quit()

    def prepare_two_programmers(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/add_programmer')
        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_names')
        element.send_keys('Kory Kraft')
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmer').click()
        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_names')
        element.send_keys('Jason Wickstra')
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmer').click()
