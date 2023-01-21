import unittest
from projects.calculator.calculator import Calculator

calculator = Calculator()

class TestSum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(4,5), 9)


if __name__ == '__main__':
    unittest.main()
