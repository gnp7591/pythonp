from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.saucedemo.com/v1/")

title = driver.title
print(title)
#time.sleep(120)
#driver.implicitly_wait(10)

# driver.close()
