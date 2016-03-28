from unittest import main, TestCase
from pascal_v1 import pascal

class TestExplicit(TestCase):
    def test_n0(self):
        self.assertEqual(list(pascal(0)), [1])

    def test_n1(self):
        self.assertEqual(list(pascal(1)), [1, 1])

    def test_n5(self):
        self.assertEqual(list(pascal(5)), [1, 5, 10, 10, 5, 1])

if __name__ == '__main__':
    main()
