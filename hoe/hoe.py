from selenium import webdriver
from capturer import Capturer

class Hoe:

    def capture(self, url):
        with Capturer() as capturer:
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

