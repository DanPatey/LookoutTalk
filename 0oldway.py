# tests.py
import unittest
from ddt import ddt, data
from mycode import larger_than_two
 
class FooTestCase(unittest.TestCase):
 
    def test_larger_than_two(self):
        self.assertTrue(larger_than_two(3))
 
    def test_not_larger_than_two(self):
        self.assertFalse(larger_than_two(1))
