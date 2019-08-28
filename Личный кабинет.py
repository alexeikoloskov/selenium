from selenium import webdriver
from time import sleep


browser = webdriver.Chrome(r"C:/ChromeDriver/chromedriver.exe")
browser.get("https://rostov.tele2.ru/")
browser.implicitly_wait(10)


def login():
    sleep(1)
    login = "9085026933"
    browser.find_element_by_xpath('//*[@id="phone-password"]').send_keys(login)
    password = "13579parol13579"
    sleep(1)
    browser.find_element_by_xpath('//*[@id="password-field"]').send_keys(password)
    sleep(1)
    browser.find_element_by_xpath('//*[@id="password-form"]/div[4]/div[1]/input').click()
def summ():
    title = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span[1]/span').text
    value = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span[2]/span').text
    print(title + " " + value)
def result():
    browser.find_element_by_xpath('//a[@class="prev icon-left-arrow"]').click()
    summ()
def residue():
    internet = browser.find_element_by_xpath('//*[@class="remnant internet"]').text
    calls = browser.find_element_by_xpath('//*[@class="remnant calls"]').text
    sms = browser.find_element_by_xpath('//*[@class="remnant sms"]').text
    print("Остаток:", internet + " ГБ", calls + " минут", sms + " SMS", sep='\n')



#Личный кабинет. 1.
browser.find_element_by_xpath('//span[@class="ico icon-login"]').click()
iframe = browser.find_element_by_xpath('//*[@id="loginDialog"]/div/div[2]/iframe')
browser.switch_to.frame(iframe)
browser.find_element_by_xpath('//*[@id="card-auth"]/div/div/ul/li[2]/a/span[2]').click()
login()

#Личный кабинет. 2.
browser.find_element_by_xpath('//span[@class="ico icon-profile"]').click()
sleep(7)
balance = browser.find_element_by_xpath('//span[@class="number"]')
print("Баланас: "+balance.text)
residue()

#Личный кабинет. 3.
browser.find_element_by_link_text('Расходы').click()
summ()
for i in range(5):
    result()


browser.quit()