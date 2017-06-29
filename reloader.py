import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

RELOAD_INTERVAL = 5 * 60

if 

url = sys.argv[1]

options = Options()
options.add_argument("--kiosk")
options.add_argument("--app=" + url)
options.add_argument("disable-infobars")

while(True):
	driver = webdriver.Chrome(chrome_options=options)
	driver.get(url)
	time.sleep(RELOAD_INTERVAL)
	# driver.close()
	driver.quit()