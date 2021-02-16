from selenium import webdriver

PATH = r"C:\Users\ivanilla\Desktop\V1PER\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.website.com")