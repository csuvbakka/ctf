from cipher import encrypt
import unittest


class TestEncryption(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual('bcd', encrypt('abc', 1))
        self.assertEqual('klm', encrypt('abc', 10))
        self.assertEqual('klM', encrypt('abC', 10))

    def test_simple_cases_negative_shift(self):
        self.assertEqual(encrypt('ccc', -1), 'bbb')
        self.assertEqual(encrypt('klm', -10), 'abc')

    def test_restarts_if_reaches_the_end_of_the_alphabet(self):
        self.assertEqual(encrypt('xyz', 1), 'yza')
        self.assertEqual(encrypt('xYz', 3), 'aBc')
        self.assertEqual(encrypt('XYZ', 1), 'YZA')
        self.assertEqual(encrypt('XYz', 3), 'ABc')

    def test_restarts_if_reaches_the_beginning_of_the_alphabet(self):
        self.assertEqual(encrypt('abc', -3), 'xyz')
        self.assertEqual(encrypt('aBC', -1), 'zAB')
        self.assertEqual(encrypt('mno', -17), 'vwx')
        self.assertEqual(encrypt('mNo', -17), 'vWx')

    def test_skips_non_alpha_characters(self):
        self.assertEqual(encrypt('abc123def', 1), 'bcd123efg')
        self.assertEqual(encrypt('aBC1 3deF!#', 2), 'cDE1 3fgH!#')
