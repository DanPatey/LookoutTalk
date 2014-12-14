import unittest

from ddt import ddt, data, unpack


@ddt
class TestName(unittest.TestCase):
        
    
    # simple decorator usage:
    list1 = [1, 2, 3, 4]
    @data(*list1)
    def test_greater_than_zero(self, value):
      self.assertGreater(value, 0)
        
    # passing data in tuples to achieve the 
    # scenarios from your given example:
    @data(('Bob', 'Bob'), ('Alice', 'Alice'))
    @unpack
    def test_name(self, first_value, second_value):
      name, expected_name = first_value, second_value
      self.assertEquals(name, expected_name)

if __name__ == '__main__':
      unittest.main(verbosity=2)
