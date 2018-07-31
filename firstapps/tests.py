# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase , SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
	def test_home_page_status(self):
		response = self.client.get('/')
		self.assertEquals(response.status_code,200) #200 la code bao loi hoac trang thai trang web,404 la loi khong tim thay trang
		