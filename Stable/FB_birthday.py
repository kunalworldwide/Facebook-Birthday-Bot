from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from collections import OrderedDict
#from driverdownload import get_driver
from selenium.common.exceptions import NoSuchElementException



chrome_options = Options()
chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})

user_id=input("Enter user ID ")
password=getpass.getpass(prompt="Enter password ")


driver= webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
driver.get('https://m.facebook.com')

def wish_birthday():
    try:
        textbox=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/form/table/tbody/tr/td[2]/div/textarea')
        textbox.send_keys("Wishing you a happy birthday!!!! stay blessed.")
        post_button=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/form/table/tbody/tr/td[3]/div/input')
        post_button.click()   
    except NoSuchElementException:
        print ("timeline posting blocked")
        return False
    return True

def get_birthday_list():
    birthday_list=[]
    driver.get('https://m.facebook.com/birthdays')
    sleep(10)
    birthdays = driver.find_elements_by_xpath('//*[@id="events_dashboard_calendar_container"]/div/article[1]/div//a')
    for birthday in birthdays:
        birthday_list.append(birthday.get_attribute("href"))
    birthday_list = list(OrderedDict.fromkeys(birthday_list))  #removing duplicate entries
    return birthday_list

user_box = driver.find_element_by_id("m_login_email")       # For detecting the user id box
user_box.send_keys(user_id)   
password_box = driver.find_element_by_id("m_login_password")    # For detecting the password box
password_box.send_keys(password) 

sleep(30) #The wait is to enter authintication code like 2 factors etc..

friends_name=get_birthday_list()

print(friends_name)

for link in friends_name:
    driver.get(link)
    result = wish_birthday()
    print(link + " birthday wish :  " + str(result))
    sleep(10)
