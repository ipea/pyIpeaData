from ipeaData.ipeadata import *
import unittest

class TestApi(unittest.TestCase):

    def test_ipeadata(self):
        self.assertIsNotNone(ipeadata('ADMIS'))

    def test_ipeadata_groupby(self):
        df = ipeadata('COMP', 'Estados')
        self.assertIsNotNone(df)
        self.assertEqual(27, df.shape[0])
        df = ipeadata('COMP', 'nadanan')
        self.assertIsNone(df)

    def test_get_sources(self):
        self.assertIsNotNone(get_sources())

    def test_get_metadata(self):
        self.assertIsNotNone(get_metadata('ADMIS'))
        self.assertIsNotNone(get_metadata())

    def test_get_region(self):
        df = get_nivel_region('QUANTLEITE')
        self.assertIsNotNone(df)
        self.assertEqual(13, df.shape[0])

if __name__ == '__main__':
    unittest.main(verbosity=3)