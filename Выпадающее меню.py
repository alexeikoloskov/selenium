from selenium import webdriver
from time import sleep

browser = webdriver.Chrome("C:/ChromeDriver/chromedriver.exe")
browser.get("https://rostov.tele2.ru/")
browser.implicitly_wait(10)



def arrow(h):
    browser.find_elements_by_xpath('//a/span[@class="ico icon-right-arrow"]')[h].click()
def tak(i):
    browser.find_elements_by_xpath('//ul[@class="regular"]/li[a]')[i].click()
    sleep(2)
def menu():
    sleep(2)
    browser.find_element_by_xpath('//span[@class="ico icon-menu"]').click()
def mobile():
    i = 0
    for x in range(12):
        menu()
        arrow(0)
        tak(i)
        browser.back()
        i = i+1
    sleep(1)
def service():
    i = 0
    for x in range(8):
        menu()
        arrow(1)
        tak(i)
        browser.back()
        i = i + 1
    sleep(1)
def support():
    i = 0
    for x in range(5):
        menu()
        arrow(2)
        tak(i)
        browser.back()
        i = i + 1
    sleep(1)
def payment():
    i = 0
    for x in range(3):
        menu()
        arrow(3)
        tak(i)
        browser.back()
        i = i + 1
    sleep(1)







mobile()
service()
support()
payment()
browser.quit()





















