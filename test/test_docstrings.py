import unittest
import doctest
import simple_demo

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(simple_demo))
    return tests
