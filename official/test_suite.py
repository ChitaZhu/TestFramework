#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhuxudan
@Contact: zhuxudan@cloudwalk.cn
@License: Mulan PSL
@Software: VSCode
@File: test_suite.py
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
    
    def upper_test(self):
        print("[{}][upper_test]".format(__name__))
        self.assertEqual('foo'.upper(), 'FOO')


# def suite_testclass():
#     print("[{}][suite_testclass]".format(__name__))
#     suite = unittest.TestSuite()
#     suite.addTest(TestStringMethods('test_upper'))
#     suite.addTest(TestStringMethods('test_isupper'))
#     return suite

# def suite_testsuite():
#     print("[{}][suite_testsuite]".format(__name__))
#     suite1 = unittest.TestSuite()
#     suite1.addTest(TestStringMethods('test_upper'))
#     suite1.addTest(TestStringMethods('test_isupper'))

#     suite2 = unittest.TestSuite()
#     suite2.addTest(TestStringMethods('test_upper'))
#     suite2.addTest(TestStringMethods('test_split'))

#     suite = unittest.TestSuite()
#     suite.addTest(suite1)
#     suite.addTest(suite2)
#     return suite

# def suite_testclass_testsuite():
#     print("[{}][suite_testclass_testsuite]".format(__name__))
#     suite1 = unittest.TestSuite()
#     suite1.addTest(TestStringMethods('test_upper'))
#     suite1.addTest(TestStringMethods('test_isupper'))

#     suite = unittest.TestSuite()
#     suite.addTest(suite1)
#     suite.addTest(TestStringMethods('test_split'))
#     return suite

# def suite_addTests():
#     print("[{}][suite_addTests]".format(__name__))
#     suite = unittest.TestSuite()
#     suite.addTests([TestStringMethods('test_upper'), TestStringMethods('test_isupper')])
#     return suite

# def suite_testLoader():
#     print("[{}][suite_testLoader]".format(__name__))
#     suite = unittest.TestSuite()
#     # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestStringMethods))
#     suite.addTests(unittest.TestLoader().loadTestsFromModule("official.test_suite"))
#     return suite



# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite_testclass())
#     runner.run(suite_testsuite())
#     runner.run(suite_testclass_testsuite())
#     runner.run(suite_addTests())
#     runner.run(suite_testLoader())
