from capturer import Capturer
from probe import Probe
from selenium import webdriver

class Hoe:
    def __init__(self, browserFactory):
        self.browserFactory = browserFactory 

    def capture(self, url):
        with self.browserFactory.get() as browser:
            capturer = Capturer(browser)
            capturer.capture(url)
            return capturer.get_base64_png()

    def save_to_html(self, url, file_name):
        image_buffer = self.capture(url)
        template = '''
        <html><head></head>
        <body>
        <img alt='page view' src='data:image/png;base64,%s'/>
        </body>
        </html>
        '''
        with open(file_name, 'wb') as f:
            f.write(template % image_buffer)

    def get_sub_url(self, base_url, url):
        probe = Probe()
        probe.open(url)
        return probe.get_internal_url()


