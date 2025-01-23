import math
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	book_button = browser.find_element(By.ID, "book")
	WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
	book_button.click()
#	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
	x = int(x_element.text)
	y = calc(x)
	math_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
	math_answer.send_keys(y)

	submit_button = browser.find_element(By.ID, "solve")
	submit_button.click()

	alert = browser.switch_to.alert
	addToClipBoard = alert.text.split()[-1]
	pyperclip.copy(addToClipBoard)
	print(addToClipBoard)


finally:
	browser.quit()
