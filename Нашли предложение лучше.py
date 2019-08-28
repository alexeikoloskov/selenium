from selenium import webdriver
from time import sleep

browser=webdriver.Chrome("C:/ChromeDriver/chromedriver.exe")
browser.get("https://rostov.tele2.ru/")
browser.implicitly_wait(20)
window_start = browser.window_handles[0]

def need_frame():
    element = browser.find_element_by_xpath('//*[@class="flocktory-widget"]')
    element.click()
    browser.switch_to.frame(element)
def screenshot():
    browser.switch_to.window(window_first)
    browser.save_screenshot('Правила программы.png')
def screenshot2():
    browser.switch_to.window(window_second)
    browser.save_screenshot('Персональные данные.png')


# Нашли предложение лучше. 1.
need_frame()
browser.find_element_by_xpath('//*[@id="tel"]').send_keys(9085026933)
name = 'Roman'
browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
sleep(2)
browser.find_element_by_xpath('/html/body/section/section[1]/a').click()
sleep(1)

#Нашли предложение лучше. 2.
browser.find_element_by_xpath('/html/body/section/div/section/div[2]/button').click()
browser.find_element_by_xpath('/html/body/section/section[1]/form/div[3]/p/a[1]').click()
window_first = browser.window_handles[1]
browser.find_element_by_xpath('/html/body/section/section[1]/form/div[3]/p/a[2]').click()
window_second = browser.window_handles[2]
browser.switch_to.default_content()


screenshot()
screenshot2()
browser.quit()


