# access search bar on ZEIT online
# tutorial from: https://www.youtube.com/watch?v=b5jt2bhSeXs

# set up
PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(PATH) # configure webdriver to access downloaded Google Chrome driver

# open web page
driver.get("https://www.zeit.de/index")

try:
    # click consent to ads
    time.sleep(2)
    consent_button = WebDriverWait(driver,200).until(
        EC.presence_of_element_located((By.ID,"sp_message_container_446139")))
    consent_button.click()

    # click close paywall ad
    time.sleep(2)
    closePaywall_button = WebDriverWait(driver,200).until(
        EC.presence_of_element_located((By.CLASS_NAME,"paywall-footer__btn-close")))
    closePaywall_button.click()

    # search for Corona
    time.sleep(1)
    search = driver.find_element_by_id("q")
    search.send_keys("Corona")
    search.send_keys(Keys.RETURN)

    # get resulting articles
    time.sleep(1)
    main = WebDriverWait(driver,100).until(
        EC.presence_of_element_located((By.ID,"main")))
    articles = main.find_elements_by_tag_name("article")

    # print header of resulting articles
    for article in articles:
        header = article.find_element_by_class_name("zon-teaser-standard__title")
        print(header.text + "\n")

finally:
    driver.quit()
