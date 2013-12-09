#!/usr/bin/env python

import unittest

import TestApp


if __name__ == '__main__':

    MCTestSuite = unittest.defaultTestLoader.discover(start_dir='.')

    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(MCTestSuite))
