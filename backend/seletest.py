from selenium import webdriver

browser = webdriver.PhantomJS() # Get local session of firefox
browser.get("http://www.yahoo.com") # Load page
assert "Yahoo!" in browser.title
browser.get_screenshot_as_file('./test.png')

browser.close()
