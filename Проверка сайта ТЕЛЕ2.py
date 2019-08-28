from selenium import webdriver

driver = webdriver.Chrome("C:/ChromeDriver/chromedriver.exe")

#Проверка сайта Tele2. 3.
driver.get("https://msk.tele2.ru/")
driver.implicitly_wait(10)
main = driver.find_element_by_xpath('//span[@class="price"]').text
driver.find_element_by_xpath('//div[@class="ssc-tariff-box"]').click()
secondary = driver.find_element_by_xpath('//span[@class="price"]').text

if main == secondary:
   print ('\n','Стоимость тарифа "Мой онлайн+" на главной странице и на странице тарифа одинаковая.')
else:
   print('\n','Стоимость тарифа "Мой онлайн+" на главной странице и на странице тарифа:', 'На главной странице это '+main+ ' руб', 'А на странице тарифа '+secondary+' руб',sep='\n')


#Проверка сайта Tele2. 4.
driver.get("https://msk.tele2.ru/")
moscow = driver.find_element_by_xpath('//span[@class="price"]').text
driver.get("https://rostov.tele2.ru/")
rostov = driver.find_element_by_xpath('//span[@class="price"]').text

if moscow == rostov:
    print('\n','Стоимость тарифа "Мой онлайн+" в Москве и Ростове одинаковая.')
else:
    print('\n','Стоимость тарифа "Мой онлайн+" в Москве и Ростове отличается:', 'В Москве это '+moscow+ ' руб', 'В Ростове это '+rostov+' руб',sep='\n')


#Проверка сайта Tele2. 6.
driver.get("https://more.tele2.ru/")
hrefs=driver.find_elements_by_css_selector("picture source")
i=0
print('\n','Ссылки на картинки с сайта "https://more.tele2.ru/":')
for x in hrefs:
   print("https://more.tele2.ru/" + hrefs[i].get_attribute("srcset"))
   i=i+1

driver.quit()

