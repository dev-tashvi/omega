from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import winreg

company_name = []

def get_default_browser():
    try:
        # Open the Windows Registry key for HTTP associations
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice") as key:
            browser_id, _ = winreg.QueryValueEx(key, "ProgId")
            # print("ProgId:", browser_id)

        # Check the browser ID and return the corresponding browser name
        if browser_id == "IE.HTTP":
            return webdriver.Ie()
        elif browser_id == "ChromeHTML":
            return webdriver.Chrome()
        elif browser_id == "BraveHTML":
            options = webdriver.ChromeOptions()
            options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"  # Update this path to match your system
            return webdriver.Chrome(options=options)
        elif browser_id == "FirefoxHTML":
            return webdriver.Firefox()
        elif browser_id == "MSEdgeHTM":
            return webdriver.Edge()
        else:
            return "Unknown"
    except FileNotFoundError:
        return "Unknown"


driver = get_default_browser()

driver.get('https://www.google.com/maps/search/technology+company+near+me/')
actions  = ActionChains(driver)

def scroll_to_load_more(parent_div, scroll_iterations=5):
    # Scroll down multiple times
    for _ in range(scroll_iterations):
        actions.send_keys_to_element(parent_div, Keys.PAGE_DOWN).perform()
        time.sleep(0.5)  # Add a delay to control the speed

while len(driver.find_elements(By.XPATH, "//div[contains(@class, 'qBF1Pd') and contains(@class, 'fontHeadlineSmall')]")) < 50:
    time.sleep(1)
    parent_div = driver.find_element(By.XPATH, "//div[contains(@class, 'm6QErb') and contains(@class, 'DxyBCb') and contains(@class, 'kA9KIf') and contains(@class, 'dS8AEf') and contains(@class, 'ecceSd')]")
    scroll_to_load_more(parent_div, scroll_iterations=5)  # Adjust the number of scroll iterations

elems = driver.find_elements(By.XPATH, "//div[contains(@class, 'qBF1Pd') and contains(@class, 'fontHeadlineSmall')]")

for elem in elems:
    company_name.append(elem.text)

for name in range(len(company_name)):
    print(f"{name} {company_name[name]}")

# in the below loop we will perform linkdin task
driver.close()
