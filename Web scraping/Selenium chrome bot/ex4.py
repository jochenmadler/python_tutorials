# clicking cookies from website: https://orteil.dashnet.org/cookieclicker/
# tutorial from: https://www.youtube.com/watch?v=OISEEL5eBqg
# Selenium ActionChains Doc: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFRuSk9QRzhmZklmb0RCek1HZ2xqUXBZbjFKZ3xBQ3Jtc0tsNzRoZ0J2LVNfbU00NDk1MFVvQTR6akFGT3B0WlJqelhUNmZWY2NmWGxzcDAtZ3NBb2Q3c1lKNF9sek40TEFodUN1NXZyalNkTkhncEVEVHBhR21MWEllR1hlZjBTWFFNejdlcThuSXJHWVZwWDRjYw&q=https%3A%2F%2Fselenium-python.readthedocs.io%2Fapi.html%23module-selenium.webdriver.common.action_chains

# set up
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) # configure webdriver to access downloaded Google Chrome driver
driver.get("https://orteil.dashnet.org/cookieclicker/")

# get elements
driver.implicitly_wait(3)
cookie = driver.find_element_by_id("bigCookie")
score = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

# set up action chain
actions = ActionChains(driver) # set up (multiple) actions, like actions.click() and exectue them with actions.perform()
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(score.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value == count:
            upgrading = ActionChains(driver)
            upgrading.move_to_element(item)
            upgrading.click()
            upgrading.perform()