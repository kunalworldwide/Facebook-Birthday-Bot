from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


user_id='killkunal'
password='6fMUAHsvSikE#FCu9R68hh*bWGVsM^$rrLm8CK4'


cd='/media/Zone/#include_programmer/python programs/chromedriver'


driver= webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.facebook.com/login.php')


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









