import unittest
from probe import Probe

class TestProbeCheckInternal(unittest.TestCase):
    def setUp(self):
        self.probe = Probe()

    @unittest.skip('fail skip')
    def test_fail(self):
        self.assertEqual(1, 2)

    def test_absolute_internal_url(self):
        root_page_url = 'http://www.google.co.kr'
        current_url = 'http://www.google.co.kr/foo'

        result = self.probe.check_internal_url(root_page_url, current_url)

        self.assertTrue(result)

    def test_different_netloc(self):
        root_page_url = 'http://www.google.co.kr'
        current_url = 'http://foogle.co.kr/foo'

        result = self.probe.check_internal_url(root_page_url, current_url)

        self.assertFalse(result)

    def test_relative(self):
        root_page_url = 'http://www.google.co.kr'
        current_url = '/sub'

        result = self.probe.check_internal_url(root_page_url, current_url)

        self.assertTrue(result)

    def test_relative_fail(self):
        root_page_url = 'http://www.google.co.kr/sub'
        current_url = '/othersub'

        result = self.probe.check_internal_url(root_page_url, current_url)

        self.assertFalse(result)
if __name__ == '__main__':
    unittest.main()
