# navigating https://www.tidyverse.org/
# tutorial from: https://www.youtube.com/watch?v=U6gbGk5WPws

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
driver.get("https://www.tidyverse.org/")

# click through
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Packages"))
    )
    element.click() # why is this so slow to load (> 10s)?

    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"dplyr"))
    )
    element.click()

    driver.back() # go back in browser to last page - why is this so slow (>5s)?

except:
    driver.quit()
