#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhuxudan
@Contact: zhuxudan@cloudwalk.cn
@License: Mulan PSL
@Software: VSCode
@File: test_fixture_class.py
@Time: 2020/07/09
"""
import unittest

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("[{}][setUpClass]".format(__name__))
        # setUp() 方法引发异常，测试框架会认为测试发生了错误，因此测试方法不会被运行
        # assert 1 == 2 

    def test_upper(self):
        print("[{}][test_upper]".format(__name__))
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("[{}][test_isupper]".format(__name__))
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        self.assertFalse('FOO'.isupper()) 

    def test_split(self):
        print("[{}][test_split]".format(__name__))
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @classmethod
    def tearDownClass(cls):
        print("[{}][tearDownClass]".format(__name__))


if __name__ == '__main__':
    unittest.main()

# 命令行参数
# setUpClass() tearDownClass() 调用关系
# python -m unittest official\test_fixture_class.py