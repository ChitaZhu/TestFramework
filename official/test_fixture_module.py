#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhuxudan
@Contact: zhuxudan@cloudwalk.cn
@License: Mulan PSL
@Software: VSCode
@File: test_fixture_module.py
@Time: 2020/07/09
"""
import unittest


def setUpModule():
    print("[{}][setUpModule]".format(__name__))

def tearDownModule():
    print("[{}][tearDownModule]".format(__name__))


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        print("[{}][TestStringMethods][test_upper]".format(__name__))
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("[{}][TestStringMethods][test_isupper]".format(__name__))
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("[{}][TestStringMethods][test_split]".format(__name__))
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestStringMethods1(unittest.TestCase):
    
    def test_upper(self):
        print("[{}][TestStringMethods1][test_upper]".format(__name__))
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("[{}][TestStringMethods1][test_isupper]".format(__name__))
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("[{}][TestStringMethods1][test_split]".format(__name__))
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

# 命令行参数
# setUpModule() tearDownModule() 调用关系
# python -m unittest official\test_fixture_module.py