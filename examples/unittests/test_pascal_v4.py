from itertools import chain
from unittest import main, TestCase
from pascal_v1 import pascal

class TestExplicit(TestCase):
    def test_n0(self):
        self.assertEqual(list(pascal(0)), [1])

    def test_n1(self):
        self.assertEqual(list(pascal(1)), [1, 1])

    def test_n5(self):
        self.assertEqual(list(pascal(5)), [1, 5, 10, 10, 5, 1])

class TestSums(TestCase):
    def test_sum(self):
        for n in (10, 100, 1000, 10000):
            self.assertEqual(sum(pascal(n)), 2**n)

    def test_alternate_sum(self):
        for n in (10, 100, 1000, 10000):
            self.assertEqual(sum(alternate(pascal(n))), 0)

class TestAdjacent(TestCase):
    def test_generate_next_line(self):
        for n in (10, 100, 1000, 10000):
            expected = [a+b for a, b
                        in zip(chain(zero(), pascal(n)),
                               chain(pascal(n), zero()))]
            result = list(pascal(n+1))
            self.assertEqual(result, expected)

def alternate(g):
    sign = 1
    for elem in g:
        yield sign*elem
        sign = -sign

def zero():
    yield 0

if __name__ == '__main__':
    main()
