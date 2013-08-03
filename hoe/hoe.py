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

    def get_base64_image(self):
        self.image_buffer = self.browser.get_screenshot_as_base64()
        return self.image_buffer

    def save_to_html(self, file_name):
        self.image_buffer = self.browser.get_screenshot_as_base64()
        template = '''
        <html><head></head>
        <body>
        <img alt='page view' src='data:image/png;base64,%s'/>
        </body>
        </html>
        '''
        with open(file_name, 'wb') as f:
            f.write(template % self.image_buffer)

