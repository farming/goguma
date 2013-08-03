from selenium import webdriver
from collections import deque

class BrowserFactory:
    def __init__(self):
        self.browser_list = deque()

    def get(self): # must be thread safe.
        if len(self.browser_list) != 0:
            return self.browser_list.popleft()

        browser = webdriver.PhantomJS()
        browserWrapper = BrowserWrapper(browser, self)

        return browserWrapper

    def pool(self, browserWraper):
        self.browser_list.append(browserWraper)

class BrowserWrapper:
    def __init__(self, browser, browserFactory):
        self.browserFactory = browserFactory
        self.browser = browser

    def __enter__(self):
        return self.browser

    def __exit__(self, type, value, traceback):
        self.browserFactory.pool(self)
