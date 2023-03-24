# Import
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Download Chromedriver
driver_path = ChromeDriverManager().install()

# Extension Name
extension_path = 'extension_3_3_1_0.crx'
options = webdriver.ChromeOptions()
options.add_extension(extension_path)

# Driver Open
s = ChromeService(driver_path)
driver = webdriver.Chrome(service=s, options=options)

extension_page = 'chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/options/options.html'
driver.get(extension_page)
time.sleep(500)
driver.quit()
