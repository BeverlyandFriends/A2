import unittest

def mult_2(x):
    return x*2

def div_2(x):
    return x/2

class test_mult(unittest.TestCase):

    def setUp(self):
        pass

    def test_mult(self):
        self.assertEqual(mult_2(2), 4)

    def test_div(self):
        self.assertEqual(div_2(2), 1)

if __name__ == '__main__':
    unittest.main()
