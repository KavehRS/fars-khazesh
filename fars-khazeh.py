#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import pandas as pd
import numpy as np
from bs2json import bs2json
import itertools


# Chromedriver 
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get("https://www.farsnews.ir/")

# WebDriverWait wait = new WebDriverWait(driver, 10);
# WebElement element = wait.until(
#         ExpectedConditions.visibilityOfElementLocated(By.id("someid")));


# Run the Webdriver, save page an quit browser
htmltext = driver.page_source
driver.quit()

# Scroll page to load whole content
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to the bottom.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load the page
    time.sleep(2)
    # Calculate new scroll height and compare with last height.
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Parse HTML structure
soup = BeautifulSoup(htmltext, "lxml")# Extract links to news id
newsid = []
for link in soup.find_all("a",
                          class_="link link--darker link--darken u-accentColor--textDarken u-baseColor--link u-fontSize14 u-flex1"):
    authors.append(link.get('href'))


        
# titr=[]
# date=[]
# articleBody
# header category-name
# publish-time
# short-url




