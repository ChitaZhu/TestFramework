#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhuxudan
@Contact: zhuxudan@cloudwalk.cn
@License: Mulan PSL
@Software: VSCode
@File: test_subtest.py
@Time: 2020/07/09
"""
import unittest


# class NumbersTest(unittest.TestCase):
    
#     def test_even(self):
#         """
#         Test that numbers between 0 and 5 are all even.
#         """
#         for i in range(0, 6):
#             self.assertEqual(i % 2, 0)


class NumbersTest(unittest.TestCase):
    
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
