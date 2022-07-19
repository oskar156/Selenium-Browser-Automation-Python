### SET UP ###
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

profilePath = r'' #C:\Users\oscar\AppData\Roaming\Mozilla\Firefox\Profiles\...
profile = webdriver.FirefoxProfile(profilePath)

execPath = r'' #...geckodriver.exe')'
driver = webdriver.Firefox(profile, executable_path=execPath)

### FUNCTIONS ###

# # # # # 
# interact
# # # # # 
def interact(driver, lookUpMethod, lookUpString, action = None, numOfResults = None, keysToSend = None, attribute = None, secsBefore = None, secsAfter = None, attempts = None):

  if secsBefore != None:
    time.sleep(secsBefore)

  limitNumOfResults = 1
  element = []
  elementsToReturn = []
  attemptsMade = 0
  loaded = False

  if attempts == None:
    attempts = 1

  while attemptsMade <= attempts and loaded == False:

    try:

      if lookUpMethod == 'XPATH':
        elements = driver.find_elements(By.XPATH, lookUpString)
      elif lookUpMethod == 'TEXT':
        elements = driver.find_elements(By.XPATH, "//*[contains(text(), '" + lookUpString + "')]")
      elif lookUpMethod == 'ID':
        elements = driver.find_elements(By.ID, lookUpString)
      elif lookUpMethod == 'CLASS_NAME':
        elements = driver.find_elements(By.CLASS_NAME, lookUpString)

      limitNumOfResults = 1
      if numOfResults == None:
        limitNumOfResults = len(elements)
      elif numOfResults >= 1:
        limitNumOfResults = numOfResults

      e = 0
      while e < limitNumOfResults:

        if action == 'click':
          elements[e].click()
        elif action == 'send_keys':
          elements[e].send_keys(keysToSend)
        elif action == 'clear':
          elements[e].clear()
        elif action == 'clear and send_keys':
          elements[e].clear()
          elements[e].send_keys(keysToSend)
        elif action == 'get text':
          elements[e] = elements[e].text
        elif action == 'get attribute':
          elements[e] = elements[e].get_attribute(attribute)
        elif action == 'check if loaded':

          if len(elements) >= 1:
            return True
          elif attemptsMade >= attempts:
            return False

        elementsToReturn.append(elements[e])
        e += 1

      if len(elements) >= 1:
        attemptsMade = attemptsMade + 1
        loaded = True
      else:
        attemptsMade = attemptsMade + 1
        time.sleep(1)

    except:
      attemptsMade = attemptsMade + 1
      time.sleep(1)

  if action == 'check if loaded':
    if loaded == False:
      return False

  if limitNumOfResults == 1:
    elementsToReturn = elementsToReturn[0]

  if secsAfter != None:
    time.sleep(secsAfter)

  return elementsToReturn

# # # # # 
# get
# # # # # 
def get(driver, link, secsBefore = None, secsAfter = None):

  if secsBefore != None:
    time.sleep(secsBefore)
  driver.get(link)
  if secsAfter != None:
    time.sleep(secsAfter)

# # # # # 
# regexLookup
# # # # # 
def regexLookup(str, regexPatternStr, ignoreCaseBool):

  if ignoreCaseBool == True:
    regexPattern = re.compile(regexPatternStr, re.IGNORECASE)
    results = regexPattern.findall(str, re.IGNORECASE)
  elif ignoreCaseBool == False:
    regexPattern = re.compile(regexPatternStr)
    results = regexPattern.findall(str)

  return results
