import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

RELOAD_INTERVAL = 5 * 60
URL = 'http://historyofthegif.com'

options = Options()
options.add_argument("--kiosk")
options.add_argument("disable-infobars")

while(True):
	driver = webdriver.Chrome(chrome_options=options)
	driver.get(URL)
	time.sleep(RELOAD_INTERVAL)
	# driver.close()
	driver.quit()