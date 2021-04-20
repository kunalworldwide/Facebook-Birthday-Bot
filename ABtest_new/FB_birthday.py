from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from collections import OrderedDict


chrome_options = Options()
chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})

user_id=input("Enter user ID")
password=input("Enter password")


driver= webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
driver.get('https://m.facebook.com')

def wish_birthday():
    textbox=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/form/table/tbody/tr/td[2]/div/textarea')
    textbox.send_keys("Wishing you a happy birthday!!!! stay blessed.")
    post_button=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/form/table/tbody/tr/td[3]/div/input')
    post_button.click()    
    return 0

user_box = driver.find_element_by_id("m_login_email")       # For detecting the user id box
user_box.send_keys(user_id)   
password_box = driver.find_element_by_id("m_login_password")    # For detecting the password box
password_box.send_keys(password) 

sleep(60) #for 2 step otp

birthdays = driver.find_elements_by_xpath('//*[@id="events_dashboard_calendar_container"]/div/article[1]/div//a')
birthday_list=[]

for birthday in birthdays:
    birthday_list.append(birthday.get_attribute("href"))
    
birthday_list = list(OrderedDict.fromkeys(birthday_list))

for link in birthday_list:
    driver.get(link)
    wish_birthday()
    sleep(10)
