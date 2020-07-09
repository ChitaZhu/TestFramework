#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhuxudan
@Contact: zhuxudan@cloudwalk.cn
@License: Mulan PSL
@Software: VSCode
@File: test_basic.py
@Time: 2020/06/15 13:05:03
"""
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        print("====== test_upper ======")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("====== test_isupper ======")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        # self.assertFalse('FOO'.isupper()) 

    def test_split(self):
        print("====== test_split ======")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

# 命令行参数
# python -m unittest -v          # 显示详细信息
# python -m unittest -q          # 安静输出
# python -m unittest --locals    # tracebacks 输出局部变量
# python -m unittest -f          # 第一个失败或者错误发生时即停止

# python -m unittest -s official    # 指定开始搜索的目录, 默认(.)
# python -m unittest -p "basic.py"  # 匹配模块名, 默认("test*.py")