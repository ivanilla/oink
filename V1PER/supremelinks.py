from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(r"C:\Users\ivanilla\Desktop\oink\V1PER\chromedriver.exe")
browser.get("https://www.supremenewyork.com/previews/springsummer2021/all/pants")

try:
	categorylist = WebDriverWait(browser, 2).until(
		EC.presence_of_element_located((By.ID, "container"))
	)
	products = categorylist.find_elements_by_class_name("inner-article")
	for product in products:
		subproduct = product.find_element_by_class_name("name-link")
		prodlink = subproduct.get_attribute("href")
		output = (f'{subproduct.text} @ {prodlink}\n')

		with open(r"C:\Users\ivanilla\Desktop\oink\V1PER\links.txt", "a") as f:
			f.write(output)
			

finally:
	browser.quit()