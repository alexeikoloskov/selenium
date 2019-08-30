from selenium import webdriver
from time import sleep


browser = webdriver.Chrome("C:/ChromeDriver/chromedriver.exe")
browser.get("https://rostov.tele2.ru/")
browser.implicitly_wait(10)


def arrow(h):
    arrows = browser.find_elements_by_xpath('//a/span[@class="ico icon-right-arrow"]')
    arrows[h].click()
def a(i):
    browser.find_elements_by_xpath('//ul[@class="regular"]/li[a]')[i].click()
    sleep(2)
def menu():
    sleep(3)
    browser.find_element_by_xpath('//span[@class="ico icon-menu"]').click()
def tele2():
    h = 0
    browser.find_element_by_xpath('//span[@class="ico icon-menu"]').click()
    arrows = (int(len(browser.find_elements_by_xpath('//a/span[@class="ico icon-right-arrow"]'))))
    browser.find_element_by_xpath('//span[@class="ico icon-close"]').click()
    sleep(2)
    while h < arrows:
        i = 0
        browser.find_element_by_xpath('//span[@class="ico icon-menu"]').click()
        browser.find_elements_by_xpath('//a/span[@class="ico icon-right-arrow"]')[0].click()
        number = (int(len(browser.find_elements_by_xpath('//ul[@class="regular"]/li[a]'))))
        browser.find_element_by_xpath('//span[@class="ico icon-left-arrow2"]').click()
        browser.find_element_by_xpath('//span[@class="ico icon-close"]').click()
        sleep(2)
        while i < number:
            menu()
            try:
                arrow(h)
                a(i)
                browser.back()
                i = i+1
            except:
                browser.get('https://rostov.tele2.ru')
                i = i+1

        sleep(1)
        h = h+1





tele2()
browser.quit()
