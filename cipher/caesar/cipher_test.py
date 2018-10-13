from cipher import encrypt, decrypt, brute_force
import unittest


class TestEncryption(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual('bcd', encrypt('abc', 1))
        self.assertEqual('klm', encrypt('abc', 10))
        self.assertEqual('klM', encrypt('abC', 10))

    def test_simple_cases_negative_shift(self):
        self.assertEqual('bbb', encrypt('ccc', -1), 'bbb')
        self.assertEqual('abc', encrypt('klm', -10))

    def test_restarts_if_reaches_the_end_of_the_alphabet(self):
        self.assertEqual('yza', encrypt('xyz', 1))
        self.assertEqual('aBc', encrypt('xYz', 3))
        self.assertEqual('YZA', encrypt('XYZ', 1))
        self.assertEqual('ABc', encrypt('XYz', 3))

    def test_restarts_if_reaches_the_beginning_of_the_alphabet(self):
        self.assertEqual('xyz', encrypt('abc', -3))
        self.assertEqual('zAB', encrypt('aBC', -1))
        self.assertEqual('vwx', encrypt('mno', -17))
        self.assertEqual('vWx', encrypt('mNo', -17))

    def test_skips_non_alpha_characters(self):
        self.assertEqual('bcd123efg', encrypt('abc123def', 1))
        self.assertEqual('cDE1 3fgH!#', encrypt('aBC1 3deF!#', 2))


class TestDecryption(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual('abc', decrypt('bcd', 1))
        self.assertEqual('abc', decrypt('klm', 10))
        self.assertEqual('abC', decrypt('klM', 10))

    def test_simple_cases_negative_shift(self):
        self.assertEqual('ccc', decrypt('bbb', -1))
        self.assertEqual('klm', decrypt('abc', -10))

    def test_restarts_if_reaches_the_end_of_the_alphabet(self):
        self.assertEqual('xyz', decrypt('yza', 1))
        self.assertEqual('xYz', decrypt('aBc', 3))
        self.assertEqual('XYZ', decrypt('YZA', 1))
        self.assertEqual('XYz', decrypt('ABc', 3))

    def test_restarts_if_reaches_the_beginning_of_the_alphabet(self):
        self.assertEqual('abc', decrypt('xyz', -3))
        self.assertEqual('aBC', decrypt('zAB', -1))
        self.assertEqual('mno', decrypt('vwx', -17))
        self.assertEqual('mNo', decrypt('vWx', -17))

    def test_skips_non_alpha_characters(self):
        self.assertEqual('abc123def', decrypt('bcd123efg', 1))
        self.assertEqual('aBC1 3deF!#', decrypt('cDE1 3fgH!#', 2))


class TestBruteForce(unittest.TestCase):
    def test_simple_case(self):
        text = 'guvf vf gur synt: PGS{}'
        self.assertEqual((-13, 'this is the flag: CTF{}'), brute_force(text, 'CTF{}'))
