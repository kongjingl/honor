import unittest
from honor import app

class HonorTest(unittest.TestCase):
    def setUp(self):
        print'setup'
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        print 'tearDown'

    def test1(self):
        print 'test1'
    def test2(self):
        print 'test2'