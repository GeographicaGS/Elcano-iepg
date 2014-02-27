# coding=UTF8

import requests, json, sys

class Foo(object):
    """

    FOO REST Test suite.

    """
    __testSuites = dict()
    __testResults = dict()
    """Loaded test suites."""

    def __init__(self, testSuites):
        """Constructor. Gets list of test suites."""
        for ts in testSuites:
            print("Importing test suite {}").format(ts)
            __import__(ts)
            self.__testSuites[ts] = sys.modules[ts]

            
    def execute(self, testSuit, tests):
        """Executes the list of tests in testSuit."""
        print("Executing tests in test suite {}:").format(testSuit)
        for t in tests:
            test = self.__testSuites[testSuit].test["tests"][t]
            print("   Executing test {}:").format(test["name"])

            if "environ" in test:
                environ = self.__testSuites[testSuit].environ[test["environ"]]
                print(environ)
            else:
                environ = self.__testSuites[testSuit].environ["default"]
                print(environ)

            if "method" in test:
                if test["method"]=="get":
                    pass



    def __get(url, headers=None, session=None):
        """Performs a get request."""
        pass
