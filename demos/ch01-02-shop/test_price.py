import unittest
from price import format_price


class TestFormatPrice(unittest.TestCase):
    def test_small(self):
        self.assertEqual(format_price(980), "¥980")

    def test_thousands(self):
        self.assertEqual(format_price(1234), "¥1,234")


if __name__ == "__main__":
    unittest.main()
