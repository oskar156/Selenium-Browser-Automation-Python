
if 1==1:
 exe_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
 driver_path = r'E:\BROWSER AUTOMATION\geckodriver.exe'

 #############################
 ### Set Up for Firefox
 #############################
 print("Set Up for Firefox")

 import os 
 import glob
 import time 
 from datetime import datetime

 #selenium
 from selenium import webdriver 
 from selenium.webdriver import Firefox
 from selenium.webdriver.firefox.options import Options
 from selenium.webdriver.firefox.service import Service
 from selenium.webdriver.common.by import By #for selenium’s find_element
 from selenium.webdriver.common.keys import Keys #send CTRL, DEL, etc... to an element
 
 #https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html
 from selenium.webdriver import ActionChains #	automate low level interactions such as mouse movements, mouse button actions, key press, and context menu interactions.
 
 from selenium.webdriver.support.ui import WebDriverWait #help check webpage loaded
 from selenium.webdriver.support import expected_conditions as EC
 
 #copy/paste interaction
 try:
   import pyperclip as pc
 except Exception as e:
   print('Unable to import pyperclip, which may be needed for some actions like importing large blocks of text quickly (eg importing HTML code into CleanSender).')
   print(e)
 
 #windows keystroke automation
 try:
   import win32api
   import win32com.client
 except Exception as e:
   print('Unable to import win32api, which may be needed for some actions like interacting with the file-upload popup (eg importing contact lists into iPost).')
   print(e)
 
 
 
 #set up options and service
 options = Options()
 options.binary_location = exe_path
 
 service = Service(driver_path)
 
 #not needed, unless we ever need a script to remember a profile's settings
 #profile_path = ff_profile_path
 #options.set_preference('profile', profile_path)
 
 #opens an instance of the browser
 driver = webdriver.Firefox(service=service, options=options)
 
 #############################
 ### FUNCTION DEFINITIONS
 #############################
 
 ##########################################################
 # do
 #     -interact with elements in a more concise way
 def do(xpath, action="find", send_keys="", wait_before = 0, attempts = 5, user_present = False, driver=driver):
     
   if wait_before > 0:
     time.sleep(wait_before)
     
   done = False
   again = True
   
   while again == True:
     
     attempt = 0
     
     while done == False and attempt < 5:
 
       andon = False
       element = None
     
       if andon == False:
         try:
           element = driver.find_element(By.XPATH, xpath)
         except Exception as e:
           print(e)
           print("Unable to find " + str(xpath))
           andon = True
       
     
       if andon == False:
         try:
           if action == "click": #click the element
             element.click()
           elif action == "send_keys": #send text to the element
             element.send_keys(send_keys)
           elif action == "clear": #clear the text in the element
             element.clear()
           elif action == "text": #return the text of the element
             return element.text
           elif action == "find": #return the element
             return element
           else:
             try:
               raise ValueError("Invalid value in action parameter. Must be a string. List of valid actions: click, send_keys, clear, text, find (or blank, which defaults to find). See function definition for more details.")
             except Exception as e:
               print(e)
               return
           done = True #success!
         except Exception as e:
           print(e)
           print("Unable to " + str(action) + " " + str(xpath))
           
           andon = True
           again = False
     
       if andon == True:
         print("Attempt " + str(attempt + 1) + "/" +  str(attempts) + " failed!")
         time.sleep(1)
       
       attempt = attempt + 1
       andon = False
       
     if user_present == True and done == False:
       user_choice = input("Enter y to skip, enter anything to try again... ")
       
       if str(user_choice).upper() == 'Y':
         again = False
       else:
         again = True
         andon = False
         
     else:
       again = False
       
       
     
 
 
 ##########################################################
 # dos
 #     -interact with elements in a more concise way (but plural)
 def dos(xpath, action="find", send_keys="", wait_before = 0, attempts = 5, user_present = False, driver=driver):
     
   if wait_before > 0:
     time.sleep(wait_before)
     
   done = False
   again = True
   
   while again == True:
     
     attempt = 0
     
     while done == False and attempt < 5:
 
       andon = False
       element = None
     
       if andon == False:
         try:
           elements = driver.find_elements(By.XPATH, xpath)
         except Exception as e:
           print(e)
           print("Unable to find " + str(xpath))
           andon = True
       
     
       if andon == False:
         try:
           if action == "click": #click the element
             for element in elements:
               element.click()
           elif action == "send_keys": #send text to the element
             for element in elements:
               element.send_keys(send_keys)
           elif action == "clear": #clear the text in the element
             for element in elements:
               element.clear()
           elif action == "text": #return the text of the element
             elements_text = []
             for element in elements:
               elements_text.append(element.text)
             return elements_text
           elif action == "find": #return the element
             return elements
           else:
             try:
               raise ValueError("Invalid value in action parameter. Must be a string. List of valid actions: click, send_keys, clear, text, find (or blank, which defaults to find). See function definition for more details.")
             except Exception as e:
               print(e)
               return
           done = True #success!
         except Exception as e:
           print(e)
           print("Unable to " + str(action) + " " + str(xpath))
           
           andon = True
           again = False
     
       if andon == True:
         print("Attempt " + str(attempt + 1) + "/" +  str(attempts) + " failed!")
         time.sleep(1)
       
       attempt = attempt + 1
       andon = False
       
     if user_present == True and done == False:
       user_choice = input("Enter y to skip, enter anything to try again... ")
       
       if str(user_choice).upper() == 'Y':
         again = False
       else:
         again = True
         andon = False
         
     else:
       again = False
       
 
 ##########################################################
 # test
 #     -check if something is possible or loaded-in a more concise way
 #     -returns true if action is possible/false if it runs into an error
 def test(xpath, action, attempts = 1, wait_per_attempt = 0, wait_before = 0, driver=driver):
   if wait_before > 0:
     time.sleep(wait_before)
     
   attempts_taken = 0
   
   while attempts_taken < attempts:
     
     print("Attempt " + str(attempts_taken + 1) + " of " + str(attempts) + "... ")
     try:
         
       element = driver.find_element(By.XPATH, xpath)
       
       if action == "find": #can the element be found?
         return True
       
       if action == "click": #can the element be clicked?
         try:
           element.click()
           return True
         except:
           print("Unable to click element!")
           
       elif action == "send_keys": #can the element be sent keys?
         try:
           element.send_keys("")
           return True
         except:
           print("Unable to send keys to element!")
         
       #commented out because: is there a way to check if clear() would work without actually clearing the element?
       #elif action == "clear":
         #element.clear()
         
       elif action == "text": #can the element's text be returned?
         try:
           value = element.text
           return True
         except:
           print("Unable to return text from element!")
       else:
         print("Invalid value in action parameter. Must be a string. List of valid actions: click, send_keys, text, find. See function definition for more details.")
 
     except:
       print("Unable to find element!")
 
     
     if wait_per_attempt > 0:
       time.sleep(wait_per_attempt)
     
     attempts_taken = attempts_taken + 1
     
   return False
    
 ##########################################################
 # go
 #     -same as driver.get() but built in wait helps make it more concise
 def go(url, wait_before = 0, driver=driver):
   if wait_before > 0:
     time.sleep(wait_before)
   driver.get(url)



