from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})



user_id='killkunal'
password='6fMUAHsvSikE#FCu9R68hh*bWGVsM^$rrLm8CK4'


cd='/media/Zone/#include_programmer/python programs/chromedriver'


driver= webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
driver.get('https://m.facebook.com')
user_box = driver.find_element_by_id("m_login_email")       # For detecting the user id box
user_box.send_keys(user_id)   

password_box = driver.find_element_by_id("m_login_password")    # For detecting the password box
password_box.send_keys(password)  


sleep(60)

driver.get('https://m.facebook.com/birthdays')
'''
birthdays = driver.find_elements_by_xpath('//div[@id="events_dashboard_calendar_container"]')
for birthday in birthdays:
    print(birthdays.get_attribute("href"))
'''
birthdays = driver.find_elements_by_xpath("//div[@id='events_dashboard_calendar_container']//a")
for birthday in birthdays:
    print(birthdays.get_attribute("href"))

'''
birthday = driver.find_element_by_css_selector('bj cf cq')
containers=birthday.find_element_by_css_selector("[class='bj cf cq']")
containers=birthday.find_element_by_xpath('//*[@id="events_dashboard_calendar_container"]/div/article[1]/div')
birthdayslist= birthdaystoday.find_elements_by_css_selector("[class='ce cf cg']")

list=driver.find_element_by_xpath('//*[@id="events_dashboard_calendar_container"]/div/article[1]/div/ul/div[2]')

//*[@id="events_dashboard_calendar_container"]/div/article[1]/div/ul/div[2]


user_box = driver.find_element_by_id("email")       # For detecting the user id box
user_box.send_keys(user_id)                                               # Enter the user id in the box 

password_box = driver.find_element_by_id("pass")    # For detecting the password box
password_box.send_keys(password)                                          # For detecting the password in the box

login_box = driver.find_element_by_id('loginbutton')   # For detecting the Login button
login_box.click()

time.sleep(60)

right_buttons = driver.find_elements_by_xpath("//*[@class= 'cxgpxx05 sj5x9vvc']")
right_buttons[1].click()
time.sleep(1)
'''








