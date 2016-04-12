from itertools import chain
from unittest import main, skip, TestCase
from pascal_v3 import pascal

class TestExplicit(TestCase):
    def test_n0(self):
        self.assertEqual(list(pascal(0)), [1])

    def test_n1(self):
        self.assertEqual(list(pascal(1)), [1, 1])

    def test_n5(self):
        self.assertEqual(list(pascal(5)), [1, 5, 10, 10, 5, 1])

class TestFractional(TestCase):
    def test_one_third(self):
        p = pascal(1/3)
        result = [next(p) for _ in range(4)]
        expected = [1, 1/3, -1/9, 5/81]
        self.assertEqual(result, expected)

class TestSums(TestCase):
    @skip('only for integer version')
    def test_sum(self):
        for n in (10, 100, 1000, 10000):
            self.assertEqual(sum(pascal(n)), 2**n)

    @skip('only for integer version')
    def test_alternate_sum(self):
        for n in (10, 100, 1000, 10000):
            self.assertEqual(sum(alternate(pascal(n))), 0)

class TestAdjacent(TestCase):
    @skip('only for integer version')
    def test_generate_next_line(self):
        for n in (10, 100, 1000, 10000):
            expected = [a+b for a, b
                        in zip(chain(zero(), pascal(n)),
                               chain(pascal(n), zero()))]
            result = list(pascal(n+1))
            self.assertEqual(result, expected)

class TestParameters(TestCase):
    @skip('only for integer version')
    def test_negative_int(self):
        with self.assertRaises(ValueError):
            next(pascal(-1))

def alternate(g):
    sign = 1
    for elem in g:
        yield sign*elem
        sign = -sign

def zero():
    yield 0

if __name__ == '__main__':
    main()
