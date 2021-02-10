import unittest
from DataStructures.ArraysAndStrings import *

class test_arrays_and_strings(unittest.TestCase):
    def testIsUnique(self):
        self.assertFalse(is_unique("HELLO"))
        self.assertTrue(is_unique("HELlO"))

    def testIsPermutation(self):
        self.assertFalse(is_permutation("abcd", "ABCD"))
        self.assertTrue(is_permutation("abcd", "dcba"))

    def testUrlify(self):
        self.assertEqual(urlify("Mr John Smith    ", 13), list("Mr%20John%20Smith"))
        self.assertEqual(urlify_in_place("Mr John Smith    ", 13), list("Mr%20John%20Smith"))

    def testPalindromPermutation(self):
        self.assertTrue(palindrome_permutation("Tact Coa"))
        self.assertFalse(palindrome_permutation("Something"))

    def testOneAway(self):
        self.assertTrue(one_away("pale", "ple"))
        self.assertTrue(one_away("pales", "pale"))
        self.assertTrue(one_away("pale", "bale"))
        self.assertFalse(one_away("pale", "bake"))
        self.assertFalse(one_away("pale", "leap"))
        self.assertFalse(one_away("pale", "leaps"))

    def testStringCompression(self):
        self.assertEqual(string_compression("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(string_compression("abc"), "abc")
        self.assertEqual(string_compression("aabbcc"), "aabbcc")

    def testRotateMatrix(self):
        pass

    def testZeroMatrix(self):
        self.assertEqual(zero_matrix([[1, 2, 3], [4, 5, 0], [7, 8, 9]]), [[1, 2, 0], [0, 0, 0], [7, 8, 0]])

if __name__ == '__main__':
    unittest.main()