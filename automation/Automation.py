from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.get('https://getbootstrap.com/docs/5.2/forms/validation/')
#chrome_browser.find_element(by='By.CLASS_NAME', value='btn-primary')

user_firstName = chrome_browser.find_element(value='validationCustom01')
user_firstName.clear()
user_firstName.send_keys('Brandon')

user_name = chrome_browser.find_element(value='validationCustom02')
user_name.clear()
user_name.send_keys('kwamou')

user_username = chrome_browser.find_element(value='validationCustomUsername')
user_username.clear()
user_username.send_keys('bradKTC')

user_city = chrome_browser.find_element(value='validationCustom03')
user_city.clear()
user_city.send_keys('New zealand')

user_zip = chrome_browser.find_element(value='validationCustom05')
user_zip.clear()
user_zip.send_keys('75000')

chrome_browser.quit()