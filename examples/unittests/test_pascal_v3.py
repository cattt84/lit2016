from unittest import expectedFailure, main, TestCase
from pascal_v1 import pascal

class TestExplicit(TestCase):
    def test_n0(self):
        self.assertEqual(list(pascal(0)), [1])

    def test_n1(self):
        self.assertEqual(list(pascal(1)), [1, 1])

    @expectedFailure
    def test_n5(self):
        self.assertEqual(list(pascal(5)), [1, 4, 6, 4, 1])

if __name__ == '__main__':
    main()
