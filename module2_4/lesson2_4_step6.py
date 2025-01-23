from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/cats.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element(By.ID, "button")
finally:
	browser.quit()
