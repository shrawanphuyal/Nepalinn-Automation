import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
chromedriver = "C:/Users/shrawan/Desktop/chrome/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http:nepalinn.com")
driver.implicitly_wait(5)
driver.maximize_window()
driver.save_screenshot('C:/Users/shrawan/Desktop/project1/images/nepalinn.png')
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

        #page = driver.find_element_by_id("hotel_name1")
        #page.click()

        driver.find_element_by_xpath("//a[@href='http://nepalinn.com/hotel_new_solitary_lodge']/button[text()='Book']").click()
        driver.save_screenshot('C:/Users/shrawan/Desktop/project1/images/nepalinn1.png')

        driver.find_element_by_xpath("//select[@id='room_count4']/option[text()='2']").click()
        #count.select_by_value("1")
        driver.save_screenshot('C:/Users/shrawan/Desktop/project1/images/nepalinn2.png')

        driver.find_element_by_xpath("//input[@name='submit']").click()

        #driver.find_element_by_xpath("//img[@src='http://nepalinn.com/assets/images/e-sewa.png']").click()

        driver.find_element_by_id("CustomerName").send_keys("shrawan")
        driver.find_element_by_id("email").send_keys("phuyalshrawan@gmail.com")
        driver.find_element_by_id("country").send_keys("Nepal")
        driver.find_element_by_id("address").send_keys("mulpani")
        driver.find_element_by_id("phone").send_keys("9843682136")
        #driver.find_element_by_id("passport").send_keys("345666")
        driver.find_element_by_id("remarks").send_keys("well")
        click=driver.find_element_by_xpath("//input[@id='pickup_req']")
        click.click()
        driver.find_element_by_id("pickup_place").send_keys("Airport")
        driver.find_element_by_id("pickup_time").send_keys("02:00PM")
        driver.find_element_by_id("termAgreement").click()
        x=driver.find_element_by_xpath("//input[@value='Pay Deposit']")
        x.click()
        driver.save_screenshot('C:/Users/shrawan/Desktop/project1/images/nepalinn6.png')



ff = nepalinn()
ff.test()
driver.save_screenshot('C:/Users/shrawan/Desktop/project1/images/nepalinn3.png')
driver.implicitly_wait(30)
#driver.quit()

"""#driver.get("http://nepalinn.com/search/result")
#driver.save_screenshot('C:/Users/shrawan/Desktop/project1/images/nepalinn4.png')
class book():
    def test1(self):

        compare= driver.find_element_by_id("compare_check1")
        compare.click()

        compare = driver.find_element_by_id("compare_check2")
        compare.click()

        compare2 = driver.find_element_by_id("compare_details")
        compare2.click()

        driver.find_element_by_xpath("//button[@class='close']").click()

aa = book()
aa.test1()
driver.save_screenshot('C:/Users/shrawan/Desktop/project1/images/nepalinn3.png')


class searchinside():
    def test2(self):

        city1 = driver.find_element_by_name("city")
        city1.send_keys("bhaktpur")

        city2 = driver.find_element_by_id("pick1")
        city2.send_keys("2018-02-19")

        city3 = driver.find_element_by_id("pick2")
        city3.send_keys("2018-02-20")

        searchButton1 = driver.find_element_by_name("submit_search")
        searchButton1.click()



bb = searchinside()
bb.test2()"""

