import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chromedriver = "C:/Users/shrawan/Desktop/chrome/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http:nepalinn.com")
driver.implicitly_wait(10)
driver.maximize_window()
driver.save_screenshot('C:/Users/shrawan/Desktop/project1/images/nepalinn11.png')
class nepalinn():
    def test(self):

        country = driver.find_element_by_id("country")
        country.send_keys("nepal")

        city = driver.find_element_by_id("city")
        city.send_keys("pokhara")

        checkIn = driver.find_element_by_id("pick1")
        checkIn.send_keys("")

        checkOut = driver.find_element_by_id("pick1")
        checkOut.send_keys("")

        searchButton = driver.find_element_by_name("submit_search")
        searchButton.click()

ff = nepalinn()
ff.test()

class book():
     def test1(self):
            compare = driver.find_element_by_id("compare_check1")
            compare.click()

            compare = driver.find_element_by_id("compare_check2")
            compare.click()

            compare2 = driver.find_element_by_id("compare_details")
            compare2.click()

            #driver.find_element_by_xpath("//button[text()='Close']").click()
            #driver.implicitly_wait(30)

            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']")))
            element.click()

aa = book()
aa.test1()

driver.save_screenshot('C:/Users/shrawan/Desktop/project1/images/nepalinn10.png')
driver.quit()