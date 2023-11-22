#############################
### FUNCTION DEFINITIONS
#############################

##########################################################
# do
#     -interact with elements in a more concise way
def do(xpath, action, send_keys="", wait_before = 0, driver=driver):
  if wait_before > 0:
    time.sleep(wait_before)
    
  element = driver.find_element(By.XPATH, xpath)
  
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
    print("Invalid value in action parameter. Must be a string. List of valid actions: click, send_keys, clear, text, find. See function definition for more details.")

##########################################################
# do_plural
#     -interact with elements in a more concise way
def do_plural(xpath, action, send_keys="", wait_before = 0, driver=driver):
  if wait_before > 0:
    time.sleep(wait_before)
    
  elements = driver.find_elements(By.XPATH, xpath)
  
  if action == "click": #click the elements
    for element in elements:
      element.click()
  elif action == "send_keys": #send text to the elements
    for element in elements:
      element.send_keys(send_keys)
  elif action == "clear": #clear the text in elements
    for element in elements:
      element.clear()
  elif action == "text": #return the text of the elements
    elements_text = []
    for element in elements:
      elements_text.append(element.text)
    return elements_text
  elif action == "find": #return the elements
    return elements
  else:
    print("Invalid value in action parameter. Must be a string. List of valid actions: click, send_keys, clear, text, find. See function definition for more details.")
    
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
    

##########################################################
# loop_gate
#     -
def loop_gate(driver, run_data, i, last_iteration_1_indexed, data = []):

  #check if we should skip this account or not 
  #(noted by a y or n in the Run? column of the google sheet)
  
  while run_data[i] == 'n':
      
    if len(data) == 0:
      print(str(i + 1), ' skipped')
    elif len(data) >= 1:
      print(str(i + 1), ' ', data[i], ' skipped')
    
    i = i + 1
    if i >= last_iteration_1_indexed:
      print("Exit the window")
      exit()
      
  print("\n")
  print("Loop ", str(i + 1), '/', str(last_iteration_1_indexed))
  return i

