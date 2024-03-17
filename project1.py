from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

DRIVER_PATH = 'C:/chromedriver/chromedriver.exe'
company_name = []
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"executable_path={DRIVER_PATH}")

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.google.com/maps/search/technology+company+near+me/')
actions  = ActionChains(driver)

def scroll_to_load_more(parent_div, scroll_iterations=5):
    # Scroll down multiple times
    for _ in range(scroll_iterations):
        actions.send_keys_to_element(parent_div, Keys.PAGE_DOWN).perform()
        time.sleep(0.5)  # Add a delay to control the speed

while len(driver.find_elements(By.XPATH, "//div[contains(@class, 'qBF1Pd') and contains(@class, 'fontHeadlineSmall')]")) < 30:
    time.sleep(1)
    parent_div = driver.find_element(By.XPATH, "//div[contains(@class, 'm6QErb') and contains(@class, 'DxyBCb') and contains(@class, 'kA9KIf') and contains(@class, 'dS8AEf') and contains(@class, 'ecceSd')]")
    scroll_to_load_more(parent_div, scroll_iterations=5)  # Adjust the number of scroll iterations

elems = driver.find_elements(By.XPATH, "//div[contains(@class, 'qBF1Pd') and contains(@class, 'fontHeadlineSmall')]")

# in the below loop we will perform linkdin task
for elem in elems:
    company_name.append(elem.text)

print(company_name)
driver.close()
