#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhuxudan
@Contact: zhuxudan@cloudwalk.cn
@License: Mulan PSL
@Software: VSCode
@File: test_result.py
@Time: 2020/07/09
"""
import HtmlTestRunner
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        print("[{}][test_upper]".format(__name__))
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("[{}][test_isupper]".format(__name__))
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        # self.assertFalse('FOO'.isupper())    
        # assert 'FOO'.isupper == False

    def test_split(self):
        print("[{}][test_split]".format(__name__))
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
