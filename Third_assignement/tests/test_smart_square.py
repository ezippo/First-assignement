import unittest

from smart_square import square_function

class TestCore(unittest.TestCase):
    """Unittest for smart_square module"""

    def test_float(self):
        """test with floats"""
        self.assertAlmostEqual(square_function(2.),4.)

if __name__=='__main__':
    unittest.main()
