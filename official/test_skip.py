#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhuxudan
@Contact: zhuxudan@cloudwalk.cn
@License: Mulan PSL
@Software: VSCode
@File: test_skip.py
@Time: 2020/07/09
"""
import sys
import unittest

__version__ = (0.1, 1)
print(sys.platform)


# 跳过测试方法
class MyTestCase(unittest.TestCase):

    # @unittest.skip("setUpClass skipping")
    @classmethod
    def setUpClass(cls):
        print("[{}][setUpClass]".format(__name__))
    
    # def setUp(self):
    #     print("[{}][setUp]".format(__name__))
    
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        print("[{}][test_windows_support]".format(__name__))
        # windows specific testing code
        pass

    def test_maybe_skipped(self, condition=False):
        if not condition:
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass

    # @unittest.skip("tearDown skipping")
    # def tearDown(self):
    #     print("[{}][tearDown]".format(__name__))

    # @unittest.skip("tearDownClass skipping")
    @classmethod
    def tearDownClass(cls):
        print("[{}][tearDownClass]".format(__name__))


# 跳过测试类
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass


# 命令行
# python -m unittest official\test_skip.py 