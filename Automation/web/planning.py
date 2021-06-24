from selenium import webdriver
from time import sleep

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://ao.roc-dev.com/AO/planning")

driver.find_element_by_xpath(("//*[@id=\"identifierId\"]")).send_keys(("je roc-dev mail moet hier "))
driver.find_element_by_xpath(("//*[@id=\"identifierNext\"]/div/button/div[2]")).click()

sleep(2)
driver.find_element_by_xpath(("//*[@id=\"password\"]/div[1]/div/div[1]/input")).send_keys(("Je wachtwoord moet hier"))
driver.find_element_by_xpath(("//*[@id=\"passwordNext\"]/div/button/div[2]")).click()

sleep(2)
driver.find_element_by_xpath(("//*[@id=\"planning_gehaald\"]")).click()
sleep(1)
driver.find_element_by_xpath(("//*[@id=\"planning_gehaald\"]/option[3]")).click()

driver.find_element_by_xpath(("//*[@id=\"waarom_niet_gelukt\"]")).send_keys("Te weinig tijd")
driver.find_element_by_xpath(("//*[@id=\"select_vak\"]")).click()

sleep(1)
driver.find_element_by_xpath(("//*[@id=\"select_vak\"]/option[20]")).click()

sleep(1)
driver.find_element_by_xpath(("//*[@id=\"ticket_selector\"]")).click()

sleep(1)
driver.find_element_by_xpath(("//*[@id=\"ticket_selector\"]/option[2]")).click()
driver.find_element_by_xpath(("//*[@id=\"btn_select_ticket\"]")).click()

sleep(1)
driver.find_element_by_xpath(("//*[@id=\"submit_planning_btn\"]")).click()

