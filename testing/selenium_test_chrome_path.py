from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
import os
from time import sleep
cwd = os.getcwd()

print(cwd)


driver= webdriver.Chrome(executable_path=cwd+'home/jackreaper/Documents/Facebook-Birthday-Bot/Stable/chromedriver')
driver.get('https://www.facebook.com')
sleep(20)


