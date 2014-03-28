from unittest import TestCase
from zope.testbrowser.wsgi import Browser
import zope.testbrowser.wsgi
from pyquery import PyQuery as pq

from app import app

class IntegrationTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('http://localhost/', wsgi_app=app)

    def test_index_page_has_correct_heading(self):
        self.browser.open("/")
        page = pq(self.browser.contents)
        self.assertEqual(page.find('h1')[0].text, "Hello World!")

    def test_hello_page_has_correct_heading(self):
        self.browser.open("/hello")
        page = pq(self.browser.contents)
        self.assertEqual(page.find('h1')[0].text, "Hello Stranger!")
