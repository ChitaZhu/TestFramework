#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhuxudan
@Contact: zhuxudan@cloudwalk.cn
@License: Mulan PSL
@Software: VSCode
@File: basic.py
@Time: 2020/06/15 13:05:03
"""
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

# 1. unittest.main() => python official\basic.py
# if __name__ == '__main__':
#     unittest.main()

# 2. 命令行接口
# 命令行路径 TestFramework\official > ...
# python -m unittest    # == python -m unittest discover; Ran 0 tests
# python -m unittest basic.py
# python -m unittest basic test_basic
# python -m unittest basic.TestStringMethods
# python -m unittest basic.TestStringMethods.test_split

# 命令行路径 TestFramework > ...
# python -m unittest    # == python -m unittest discover; Ran 3 tests
# python -m unittest official\basic.py
# python -m unittest official.basic test_basic
# python -m unittest official.basic.TestStringMethods
# python -m unittest official.basic.TestStringMethods.test_split

