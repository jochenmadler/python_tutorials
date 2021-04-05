# tutorial playlist here: https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ

# Download Google Chrome driver (for current version): https://sites.google.com/a/chromium.org/chromedriver/downloads
# And place it on a local PATH and add "\chromedriver.exe" 
PATH = "C:\Program Files (x86)\chromedriver.exe"

from selenium import webdriver
driver = webdriver.Chrome(PATH) # configure webdriver to access downloaded Google Chrome driver

# open a web page
driver.get("https://www.zeit.de/index")

# print tab title
print(driver.title)

# close a web page
driver.close() # closes current tab. Close the browser with driver.quit()