from capturer import Capturer
from probe import Probe
from selenium import webdriver

class Hoe:
    def __init__(self):
        self.browser = webdriver.PhantomJS()
        self.image_buffer = ''

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.browser.close()

    def open(self, url):
        self.browser.get(url)
        self.image_buffer = self.browser.get_screenshot_as_base64()

    def get_base64_image(self):
        return self.image_buffer

    def save_to_html(self, file_name):
        template = '''
        <html><head></head>
        <body>
        <img alt='page view' src='data:image/png;base64,%s'/>
        </body>
        </html>
        '''
        with open(file_name, 'wb') as f:
            f.write(template % self.image_buffer)

    def get_sub_url(self, base_url, url):
        probe = Probe()
        probe.open(url)
        return probe.get_internal_url()


