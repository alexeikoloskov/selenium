from selenium import webdriver
from time import sleep

browser = webdriver.Chrome("C:/ChromeDriver/chromedriver.exe")
browser.get("https://rostov.tele2.ru/")
browser.implicitly_wait(10)

def exit():
    browser.find_element_by_xpath('//*[@class="ico icon-left-arrow2"]').click()


browser.find_element_by_xpath('//*[@class="ico icon-menu"]').click()
sleep(2)

browser.find_element_by_link_text('Мобильная связь').click()
sleep(2)
exit()
browser.find_element_by_link_text('Сервисы').click()
sleep(2)
exit()
browser.find_element_by_link_text('Поддержка').click()
sleep(2)
exit()
browser.find_element_by_link_text('Оплата').click()
sleep(2)
exit()


browser.quit()

























