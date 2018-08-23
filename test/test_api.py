from ipeadata.api import *
import unittest


class TestApi(unittest.TestCase):

    def test_ipeadata(self):
        self.assertIsNotNone(get_data('ADMIS'))

    def test_ipeadata_groupby(self):
        df = get_data('COMP', 'Estados')
        self.assertIsNotNone(df)
        self.assertEqual(27, df.shape[0])
        df = get_data('COMP', 'nadanan')
        self.assertIsNone(df)

    def test_get_sources(self):
        self.assertIsNotNone(get_sources())

    def test_get_metadata(self):
        self.assertIsNotNone(get_metadata('ADMIS'))

    def test_get_region(self):
        df = get_region_level('QUANTLEITE')
        self.assertIsNotNone(df)
        self.assertEqual(13, df.shape[0])


if __name__ == '__main__':
    unittest.main(verbosity=3)
