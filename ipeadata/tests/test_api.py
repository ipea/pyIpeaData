from ipeadata.ipeadata import *
import unittest

class TestApi(unittest.TestCase):

    def test_ipeadata(self):
        self.assertIsNotNone(ipeadata('ADMIS'))

    def test_get_sources(self):
        self.assertIsNotNone(get_sources())

    def test_get_metadata(self):
        self.assertIsNotNone(get_metadata('ADMIS'))
        self.assertIsNotNone(get_metadata())
if __name__ == '__main__':
    unittest.main()