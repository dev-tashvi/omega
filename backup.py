from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

DRIVER_PATH = 'C:/chromedriver/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"executable_path={DRIVER_PATH}")

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.google.com/maps/search/technology+company+near+me/')
actions  = ActionChains(driver)

def scroll_to_load_more(parent_div):
    # Scroll down to the bottom of the page
    actions.send_keys_to_element(parent_div,Keys.DOWN).perform();    


while len(driver.find_elements(By.XPATH, "//div[contains(@class, 'qBF1Pd') and contains(@class, 'fontHeadlineSmall')]")) < 50:
    time.sleep(1)
    parent_div = driver.find_element(By.XPATH, "//div[contains(@class, 'm6QErb') and contains(@class, 'DxyBCb') and contains(@class, 'kA9KIf') and contains(@class, 'dS8AEf') and contains(@class, 'ecceSd')]")
    scroll_to_load_more(parent_div)


elems = driver.find_elements(By.XPATH, "//div[contains(@class, 'qBF1Pd') and contains(@class, 'fontHeadlineSmall')]")

i=0;
for elem in elems:
    i+=1;
    company_name = elem.text
    print(company_name)

driver.close()
