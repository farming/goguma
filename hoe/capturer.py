class Capturer:

    def __init__(self, browser):
        self.browser = browser;

    def capture(self, url):
        self.browser.get(url)
        self.image_buffer = self.browser.get_screenshot_as_base64()

    def get_base64_png(self):
        return self.image_buffer
