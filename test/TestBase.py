
import unittest
import sys, os

sys.path.append('..')
print sys.path
from DataMapper import DataMapper


class TestBase(unittest.TestCase):

    """ common setup and teardown for tests """

    def setUp(self):
        self.dm = DataMapper()
        

    def tearDown(self):
        pass


