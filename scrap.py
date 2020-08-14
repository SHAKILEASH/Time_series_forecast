from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import pickle 
from selenium.webdriver.chrome.options import Options

#ch_options = webdriver.ChromeOptions()
#ch_options.add_argument(r"user-data-dir = C:\Users\Shaki\AppData\Local\Google\Chrome\User Data")
#driver = webdriver.Chrome(executable_path=r'C:\Users\Shaki\scrap\chromedriver.exe', options = ch_options)
'''driver.get("https://www.bonumunion.com/account/login?href=https%3A%2F%2Fwww.bonumunion.com%2Findex")
print("driver\n\n\n",driver)
driver.refresh()
username = driver.find_element_by_xpath("//input[@placeholder='User Name']")

driver.execute_script(
"document.getElementsByClassName('van-field__control')[1].removeAttribute('readonly')");
driver.execute_script(
"document.getElementsByClassName('van-field__control')[1].value='nif'");
#driver.execute_script("$('input[type=password]');");
password = driver.find_element_by_xpath("//input[@placeholder='Password']")
print("password",password.is_displayed())
username.send_keys("6380954027")
password.send_keys("6380954027")
'''
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Shaki\AppData\Local\Google\Chrome\User Data") #Path to your chrome profile

driver = webdriver.Chrome(r'C:\Users\Shaki\scrap\chromedriver.exe', chrome_options=options)
driver.get("https://www.bonumunion.com/parity/paritycat?type=0")
#driver.get('https://www.google.com/')
'''username = driver.find_element_by_id("usr")
password = driver.find_element_by_id("pwd")'''

#username.send_keys("admin")
#password.send_keys("12345")

#driver.find_element_by_xpath("//input[@type='submit']").click()
#pickle.dump(driver.get_cookies() , open("QuoraCookies.pkl","wb")) 
'''for cookie in pickle.load(open("QuoraCookies.pkl", "rb")): 
    driver.add_cookie(cookie)'''

#driver.find_element_by_name("Login Imediately").click()
#browser = webdriver.Firefox(r'C:\Program Files\Mozilla Firefox\firefox.exe')
