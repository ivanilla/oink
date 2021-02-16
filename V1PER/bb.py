from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user_search = input('Which item to search on Best Buy?')

PATH = r"C:\Users\ivanilla\Desktop\V1PER\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.bestbuy.com/")
print(driver.title)

#Close email popup
driver.find_element_by_xpath("//*[@class='c-close-icon  c-modal-close-icon']").click();

searchbar = driver.find_element_by_id("gh-search-input")
searchbar.click()
searchbar.send_keys(user_search)

#click search button
driver.find_element_by_xpath("//*[@class='header-search-button']").click();



#print(driver.page_source)

#wait for presence of this element before moving on!

try:
	skulist = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "sku-item-list"))
	)
	skuitems = skulist.find_elements_by_class_name("sku-item")
	for skuitem in skuitems:
		header = skuitem.find_element_by_class_name("sku-header")
		stock = skuitem.find_element_by_class_name("sku-list-item-button")
		print(f'{stock.text} - {header.text}')


finally:
	driver.quit()
	