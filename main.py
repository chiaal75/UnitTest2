import pyToBeTested
import unittest
import pytest

print(pyToBeTested.product(5,1))

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        '''test_upper'''
        self.assertEqual(pyToBeTested.product(20,0), 0)

    def test_lower(self):
        '''test_lower'''
        self.assertEqual(pyToBeTested.product(20,0), 5)

if __name__ == '__main__':
 unittest.main()

#print(TestStringMethods.test_upper.__doc__)