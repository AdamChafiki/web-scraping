from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("chromedriver.exe")
browser = webdriver.Chrome(service=service)


browser.get("https://accounts.google.com/signin")

wait = WebDriverWait(browser, 10)
emailElem = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))


emailElem.send_keys("not_my_real_email@gmail.com")
emailElem.send_keys(Keys.ENTER)
passwordElem = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
passwordElem.send_keys("your_password_here")
passwordElem.send_keys(Keys.ENTER)
