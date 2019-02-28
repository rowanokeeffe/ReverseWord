#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import ReverseWords
 
class TestExample(unittest.TestCase):
    def setUp(self):
        pass
 
    def test_getReversedString(self):
        self.assertEqual(ReverseWords.getReversedString("This is an example!"),"sihT si na !elpmaxe" )
        self.assertEqual(ReverseWords.getReversedString("double  spaces"), "elbuod  secaps")

if __name__ == '__main__':
    unittest.main()