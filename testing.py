import unittest
from add import add
from mul import multiplication
from sub import sub


class Tests(unittest.TestCase):

    def test_1(self):
        """Check that add is working"""
        self.assertEqual(add(3,4),7)

    def test_2(self):
        """check that multiplication is working"""
        self.assertEqual(multiplication(3,4), 12)
    def test_3(self):
        """check that Substraction is working"""
        self.assertEqual(sub(4,3),1)


    

if __name__ == "__main__":
    unittest.main()