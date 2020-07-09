#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhuxudan
@Contact: zhuxudan@cloudwalk.cn
@License: Mulan PSL
@Software: VSCode
@File: test_basic1.py
@Time: 2020/06/15 13:05:03
"""
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print("====== setUp ======")
        # assert 1 == 2

    def test_upper(self):
        print("====== test_upper ======")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("====== test_isupper ======")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        self.assertFalse('FOO'.isupper()) 

    def test_split(self):
        print("====== test_split ======")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    def tearDown(self):
        print("====== tearDown ======")


if __name__ == '__main__':
    unittest.main()

# 命令行参数
# python -m unittest official\test_basic1.py