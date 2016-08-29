import doctest
import simple_demo

# pylint: disable=unused-argument
def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(simple_demo))
    return tests
