
#############################
### Set Up for Chrome
#############################
print("Set Up for Chrome")

import os 
import glob
import time 

#selenium
from selenium import webdriver 
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #for selenium’s find_element
from selenium.webdriver.common.keys import Keys #send CTRL, DEL, etc... to an element

from selenium.webdriver.support.ui import WebDriverWait #help check webpage loaded
from selenium.webdriver.support import expected_conditions as EC

#copy/paste interaction
try:
  import pyperclip as pc
except:
  print('Unable to import pyperclip, which may be needed for some actions.')

#set up options and service
options = Options()
options.binary_location = exe_path

service = Service(driver_path) #https://googlechromelabs.github.io/chrome-for-testing/ > https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.92/win32/chromedriver-win32.zip

#not needed, unless we ever need a script to remember a profile's settings
#profile_path = ff_profile_path
#options.set_preference('profile', profile_path)

#opens an instance of the browser
driver = webdriver.Chrome(service=service, options=options)

