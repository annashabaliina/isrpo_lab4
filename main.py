import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        resa = area(10, 0)
        resp = perimeter(10, 0)
        self.assertEqual(resa, 0)
        self.assertEqual(resp, 20)
    def test_square_mul(self):
        resa = area(10, 10)
        resp = perimeter(10, 10)
        self.assertEqual(resa, 100)
        self.assertEqual(resp, 40)

if __name__ == "__main__":
  unittest.main()
