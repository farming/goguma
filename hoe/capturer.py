from selenium import webdriver

class Capturer:

    def __enter__(self):
        self.browser = webdriver.PhantomJS()
        return self

    def __exit__(self, type, value, traceback):
        self.browser.close()

    def capture(self, url):
        self.browser.get(url)
        self.image_buffer = self.browser.get_screenshot_as_base64()

    def get_base64_png(self):
        return self.image_buffer
