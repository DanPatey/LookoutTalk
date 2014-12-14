# tests.py
import unittest
from ddt import ddt, data
from mycode import larger_than_two
 
@ddt
class FooTestCase(unittest.TestCase):
 
    @data(3, 4, 12, 23)
    def test_larger_than_two(self, value):
        self.assertTrue(larger_than_two(value))
 
    @data(1, -3, 2, 0)
    def test_not_larger_than_two(self, value):
        self.assertFalse(larger_than_two(value))
