from selenium import webdriver
from selenium.webdriver.common.by import By
import time

DRIVER_PATH = 'C:/chromedriver/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"executable_path={DRIVER_PATH}")

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.google.com/maps/search/technology+company+near+me/')

def scroll_to_load_more(parent_div):
    # Scroll down to the bottom of the page
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", parent_div)
    time.sleep(3)  # Wait for some time to let new content load


while len(driver.find_elements(By.XPATH, "//div[contains(@class, 'qBF1Pd') and contains(@class, 'fontHeadlineSmall')]")) < 50:
    parent_div = driver.find_element(By.XPATH, "//div[contains(@class, 'm6QErb') and contains(@class, 'DxyBCb') and contains(@class, 'kA9KIf') and contains(@class, 'dS8AEf') and contains(@class, 'ecceSd')]")
    scroll_to_load_more(parent_div)


elems = driver.find_elements(By.XPATH, "//div[contains(@class, 'qBF1Pd') and contains(@class, 'fontHeadlineSmall')]")

i=0;
for elem in elems:
    i+=1;
    company_name = elem.text
    print(company_name)

driver.close()
