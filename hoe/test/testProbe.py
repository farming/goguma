import unittest
from probe import Probe

class TestProbeCheckInternal(unittest.TestCase):
    def setUp(self):
        self.probe = Probe()
        self.probe.url = 'http://www.google.co.kr'

    @unittest.skip('fail skip')
    def test_fail(self):
        self.assertEqual(1, 2)

    def test_full_internal_url(self):
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
        current_url = 'sub'

        result = self.probe.check_internal_url(root_page_url, current_url)

        self.assertTrue(result)

    def test_relative2(self):
        root_page_url = 'http://www.google.co.kr/sub'
        current_url = 'sub'

        result = self.probe.check_internal_url(root_page_url, current_url)

        self.assertTrue(result)

    def test_absolute_fail(self):
        root_page_url = 'http://www.google.co.kr/sub'
        current_url = '/othersub'

        result = self.probe.check_internal_url(root_page_url, current_url)

        self.assertFalse(result)

class TestProbe(unittest.TestCase):
    def test_normal(self):
        internal_url_list = self.__helper__(
                root_page_path = 'http://example.com/',
                current_path = 'http://example.com/f/b',
                a_link='http://example.com/f')

        self.assertIn('http://example.com/f', internal_url_list)

    def test_same_as_root_page(self):
        internal_url_list = self.__helper__(
                root_page_path = 'http://example.com/f/',
                current_path = 'http://example.com/f/b',
                a_link='http://example.com/f/')

        self.assertIn('http://example.com/f/', internal_url_list)

    def test_relative(self):
        internal_url_list = self.__helper__(
                root_page_path = 'http://example.com/f/',
                current_path = 'http://example.com/f/b',
                a_link='./tail')

        self.assertIn('http://example.com/f/tail', internal_url_list)

    def test_relative2(self):
        internal_url_list = self.__helper__(
                root_page_path = 'http://example.com/f/',
                current_path = 'http://example.com/f/b',
                a_link='tail')

        self.assertIn('http://example.com/f/tail', internal_url_list)

    def test_absolute(self):
        internal_url_list = self.__helper__(
                root_page_path = 'http://example.com/f/',
                current_path = 'http://example.com/f/b',
                a_link='/f/awef')

        self.assertIn('http://example.com/f/awef', internal_url_list)

    def test_absolute_fail(self):
        internal_url_list = self.__helper__(
                root_page_path = 'http://example.com/f/',
                current_path = 'http://example.com/f/b',
                a_link='/asd')

        self.assertNotIn('http://example.com/asd', internal_url_list)

    def __helper__(self, a_link, current_path, root_page_path):
        probe = Probe()
        probe.parse_string(current_path,
        '''
        <html><head></head>
        <body>
        <a href="%s"></a>
        </body></html>
        ''' % a_link)

        return probe.get_internal_url(root_page_path)


if __name__ == '__main__':
    unittest.main()
