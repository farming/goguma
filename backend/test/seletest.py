import base64
from selenium import webdriver

SAVE_IMAGE = False

browser = webdriver.PhantomJS() # Get local session of firefox
browser.get("http://www.yahoo.com") # Load page
assert "Yahoo!" in browser.title

if SAVE_IMAGE:
    browser.get_screenshot_as_file('./test.png')

else:
    b64_img = browser.get_screenshot_as_base64()
    try:
        with open('./test.png', 'wb') as f:
            f.write(base64.decodestring(b64_img))
    except IOError:
        browser.close()
        exit(1)

browser.close()
