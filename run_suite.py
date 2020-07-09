#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhuxudan
@Contact: zhuxudan@cloudwalk.cn
@License: Mulan PSL
@Software: VSCode
@File: run_suite.py
@Time: 2020/07/09
"""
import os
import unittest
from official.test_suite import TestStringMethods
from official import test_suite


def suite_testclass():
    print("[{}][suite_testclass]".format(__name__))
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestStringMethods('test_isupper'))
    return suite

def suite_testsuite():
    print("[{}][suite_testsuite]".format(__name__))
    suite1 = unittest.TestSuite()
    suite1.addTest(TestStringMethods('test_upper'))
    suite1.addTest(TestStringMethods('test_isupper'))

    suite2 = unittest.TestSuite()
    suite2.addTest(TestStringMethods('test_upper'))
    suite2.addTest(TestStringMethods('test_split'))

    suite = unittest.TestSuite()
    suite.addTest(suite1)
    suite.addTest(suite2)
    return suite

def suite_testclass_testsuite():
    print("[{}][suite_testclass_testsuite]".format(__name__))
    suite1 = unittest.TestSuite()
    suite1.addTest(TestStringMethods('test_upper'))
    suite1.addTest(TestStringMethods('test_isupper'))

    suite = unittest.TestSuite()
    suite.addTest(suite1)
    suite.addTest(TestStringMethods('test_split'))
    return suite

def suite_addTests():
    print("[{}][suite_addTests]".format(__name__))
    suite = unittest.TestSuite()
    suite.addTests([TestStringMethods('test_upper'), TestStringMethods('test_isupper')])
    return suite

def suite_testLoader():
    print("[{}][suite_testLoader]".format(__name__))
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestStringMethods))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_suite))
    suite.addTests(unittest.TestLoader().loadTestsFromName('TestStringMethods', test_suite))
    suite.addTests(unittest.TestLoader().loadTestsFromName('TestStringMethods.test_isupper', test_suite))
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['TestStringMethods'], test_suite))
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['TestStringMethods.test_isupper'], test_suite))
    suite.addTests(unittest.TestLoader().discover(os.path.dirname(__file__), 'basic*.py'))
    suite.addTests(unittest.TestLoader().discover(".", 'basic*.py'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_testclass())
    runner.run(suite_testsuite())
    runner.run(suite_testclass_testsuite())
    runner.run(suite_addTests())
    runner.run(suite_testLoader())