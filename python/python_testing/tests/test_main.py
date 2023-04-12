import unittest
from ..python_testing import main


class MainTest(unittest.TestCase):
    def test_add_integer(self):
        result = main.add_integer(10, 7)
        self.assertEqual(result, 17)



if __name__ == "__main__":
    unittest.main()