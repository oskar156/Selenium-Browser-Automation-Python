print("FLASH Phone Score Update Browser Automation.py")
print("")

#task details: 
# https://app.asana.com/0/1200050614619090/1206915726973959

###################################################################
# USER INPUT SECTION, UPDATE AS NEEDED
count_name = "030624630" #REQUIRED

#IF BLANK THEN THE SCRIPT WILL GET THE QUANTITY BY ITSELF 
#any non-numeric characters will be removed, so commas are ok here
count_quantity = "250"  #OPTIONAL

#VALID OPTIONS (case-sensitive): 1PA,1PI,DMS
#IF BLANK THEN THE SCRIPT WILL DEFAULT TO 1PI 
dedupe_type = "DMS"  #OPTIONAL

#IF BLANK THEN THE SCRIPT WILL DEFAULT TO CONSUMER 
#VALID OPTIONS (case-sensitive):    Consumer, Business, Mortgage, New Movers, B2B Emails
database_name = "Consumer"   #OPTIONAL






#USUALLY LEAVE THE BELOW AS IS
exe_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver_path = r'E:\BROWSER AUTOMATION\geckodriver.exe'
flash_login_url = ''
flash_username = ''
flash_password = ''

fields_to_select = [
  'FIRST NAME',
  'MI',
  'LAST NAME',
  'PREFIX',
  'ADDRESS',
  'SUITE/APT',
  'CITY',
  'STATE',
  'ZIP5',
  'ZIP4',
  'DELIVERY POINT BAR CODE',
  'CARRIER ROUTE',
  'FIPS COUNTY CODE',
  'COUNTY NAME',
  'CENSUS MEDIAN HOME VALUE',
  'CENSUS MEDIAN HOUSEHOLD INCOME',
  'DSF DELIVERABILITY INDICATOR',
  'DELIVERY POINT DROP INDICATOR',
  'TELEPHONE PRESENT FLAG',
  'TELEPHONE NUMBER',
  'HOME OWNER SOURCE FLAG',
  'NUMBER OF LINES OF CREDIT (TRADE COUNTER)',
  'OCCUPATION',
  'OCCUPATION - DETAILED - SEE OCCUPATION APPEND',
  "Age < 1 Children's Age",
  "Age = 1 Children's Age",
  "Age = 2 Children's Age",
  "Age = 3 Children's Age",
  "Age = 4 Children's Age",
  "Age = 5 Children's Age",
  "Age = 6 Children's Age",
  "Age = 7 Children's Age",
  "Age = 8 Children's Age",
  "Age = 9 Children's Age",
  "Age = 10 Children's Age",
  "Age = 11 Children's Age",
  "Age = 12 Children's Age",
  "Age = 13 Children's Age",
  "Age = 14 Children's Age",
  "Age = 15 Children's Age",
  "Age = 16 Children's Age",
  "Age = 17 Children's Age",
  "Age = 18 Children's Age",
  'PROPERTY TYPE',
  'SENIOR ADULT IN HOUSEHOLD',
  'Males 18-24',
  'Females 18-24',
  'Unknown Gender 18-24',
  'Males 25-34',
  'Females 25-34',
  'Unknown Gender 25-34',
  'Males 35-44',
  'Females 35-44',
  'Unknown Gender 35-44',
  'Males 45-54',
  'Females 45-54',
  'Unknown Gender 45-54',
  'Males 55-64',
  'Females 55-64',
  'Unknown Gender 55-64',
  'Males 65-74',
  'Females 65-74',
  'Unknown Gender 65-74',
  'Males 75+',
  'Females 75+',
  'Unknown Gender 75+',
  'RETAIL ACTIVITY DATE OF LAST',
  'STANDARD RETAIL, MEMBERSHIP WAREHOUSE',
  'STANDARD RETAIL, CATALOG SHOWROOM / RETAIL BU',
  'STANDARD RETAIL, MAIN STREET RETAIL',
  'STANDARD RETAIL, HIGH VOLUME LOW END DEPARTME',
  'STANDARD RETAIL, STANDARD RETAIL',
  'STANDARD SPECIALTY, SPORTING GOODS',
  'STANDARD SPECIALTY, SPECIALTY APPAREL',
  'STANDARD SPECIALTY, SPECIALTY',
  'STANDARD SPECIALTY, COMPUTER / ELECTRONICS BU',
  'STANDARD SPECIALTY, FURNITURE BUYERS',
  'STANDARD SPECIALTY, HOME OFFICE SUPPLY PURCHA',
  'STANDARD SPECIALTY, HOME IMPROVEMENT',
  'UPSCALE RETAIL - HIGH END RETAIL BUYERS, UPSC',
  'UPSCALE SPECIALTY, TRAVEL / PERSONAL SERVICES',
  'BANK, FINANCIAL SERVICES - BANKING',
  'FINANCE COMPANY, FINANCIAL SERVICES - INSTALL',
  'OIL COMPANY, OIL COMPANY',
  'MISCELLANEOUS, FINANCIAL SERVICES - INSURANCE',
  'MISCELLANEOUS, TV / MAIL ORDER PURCHASES',
  'MISCELLANEOUS, GROCERY',
  'MISCELLANEOUS, MISCELLANEOUS',
  'RETAIL PURCHASES - MOST FREQUENT CATEGORY',
  'NUMBER OF ORDERS - UPSCALE CATALOGS - RNG',
  'NUMBER OF ORDERS - LOW SCALE CATALOGS - RNG',
  'NUMBER OF ORDERS - MID SCALE CATALOGS - RNG',
  'METHOD OF PAYMENT COUNT - CASH',
  'METHOD OF PAYMENT COUNT - CREDIT CARD',
  'METHOD OF PAYMENT COUNT - RETAIL CARD',
  'WEEKS SINCE LAST ONLINE ORDER',
  'WEEKS SINCE LAST OFFLINE ORDER',
  'WEEKS SINCE LAST ORDER',
  'LAST OFFLINE ORDER DATE',
  'LAST ONLINE ORDER DATE',
  'INVESTING / FINANCE GROUPING',
  'OFF-ROAD RECREATIONAL VEHICLES',
  'BOAT OWNER',
  'TRUCK OWNER',
  'MOTORCYCLE OWNER',
  'RV OWNER',
  'RV',
  'VEHICLE - NEW CAR BUYER',
  'VEHICLE - KNOWN OWNED NUMBER (NUMERIC 1 - 3;',
  'VEHICLE - NEW USED INDICATOR - 1ST VEHICLE',
  'VEHICLE - NEW USED INDICATOR - 2ND VEHICLE',
  'VEHICLE - DOMINANT LIFESTYLE INDICATOR',
  'NCOA DATE -',
  'KEY CODE',
  'Type_ncoa_return_data',
  'Primary_ncoa_return_data',
  'Pre_ncoa_return_data',
  'Street_ncoa_return_data',
  'Post_ncoa_return_data',
  'Suffix_ncoa_return_data',
  'Abrev_ncoa_return_data',
  'Secy_ncoa_return_data',
  'Pmb_ncoa_return_data',
  'Pmbno_ncoa_return_data',
  'Dpc_ncoa_return_data',
  'Dpv_ncoa_return_data',
  'HH ID',
  'INDV ID',
  'Perm ID',
  'Property Type',
  'Phone Confidence Score',
  'Phone Class - R=Residential',
  'Phone L=Land-Line V=Voip O=Other W=Wireless',
  'Phone Directory Listed',
  'Phone Verification Date (CCYYMMDD)',
  'A_CREDIT_2004',
  'Telephone 2',
  'Phone 2 Confidence Score',
  'Phone 2 Class - R=Residential',
  'Phone 2 L=Land V=Voip O=Other W=Wireless',
  'Phone 2 Directory Listed',
  'Phone 2 Verification Date (CCYYMMDD)',
  'Phone 2 DNC Flag',
  'Phone 2 - Presence of Telephone 2',
  'Child-1 Date of Birth',
  'Child-1 Gender',
  'Child-2 Date of Birth',
  'Child-2 Gender',
  'Child-3 Date of Birth',
  'Child-3 Gender',
  'Child-4 Date of Birth',
  'Child-4 Gender',
  'E-Mail Present Flag',
  'LSDI Comp-HHold ID 13 Bytes',
  'LSDI Individual ID'
]

# USER INPUT SECTION END
###################################################################

if count_name == "":
  input("count_name can't be blank! Please exit the window, open the script in a text editor and enter a count_name")
  exit()

#Consumer, Business, Mortgage, New Movers, B2B Emails
database_dropdown_value = ""
if database_name == "LCRLCR":
  database_dropdown_value = ""
elif database_name == "Consumer":
  database_dropdown_value = "LCRLCR"
elif database_name == "Business":
  database_dropdown_value = "LSBLSB"
elif database_name == "Mortgage":
  database_dropdown_value = "LM2LM2"
elif database_name == "New Movers":
  database_dropdown_value = "LNMLNM"
elif database_name == "B2B Emails":
  database_dropdown_value = "B2BB2B"
else:
  database_dropdown_value = "LCRLCR"

#############################
### Set Up for Firefox
#############################
print("SET UP FOR FIREFOX")

import os 
import re
import time 
#import glob
#from datetime import datetime

#selenium
from selenium import webdriver 
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By #for selenium’s find_element
from selenium.webdriver.common.keys import Keys #send CTRL, DEL, etc... to an element
from selenium.webdriver.support.ui import Select #makes dropdowns easier

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

service = Service(driver_path)

#opens an instance of the browser
driver = webdriver.Firefox(service=service, options=options)

#############################
### PASS WEBROOT
#############################
print("PASS WEBROOT")

try:
  allow_button = driver.find_element(By.XPATH, "//input[@id='allowButton']")
  allow_button.click()
except:
  pass

#############################
### LOGIN TO FLASH
#############################
print("LOGIN TO FLASH")

driver.get(flash_login_url)
time.sleep(0.5)

user_name_input = driver.find_element(By.XPATH, "//input[@name='username']")
user_name_input.send_keys(flash_username)

password_input = driver.find_element(By.XPATH, "//input[@name='password']")
password_input.send_keys(flash_password)

submit_button = driver.find_element(By.XPATH, "//input[@name='Login']")
submit_button.click()
time.sleep(0.5)




if count_quantity == "":
  #############################
  ### SELECT RUN COUNT
  #############################
  print("SELECT RUN COUNT")

  select = Select(driver.find_element(By.XPATH, "//select[@id='dbselect']"))
  #databse_dropdown = driver.find_element(By.XPATH, "//select[@id='dbselect']")
  #databse_dropdown.click()

  select.select_by_value(str(database_dropdown_value))
  #databse_dropdown_consumer_option = driver.find_element(By.XPATH, "//select[@id='dbselect']/option[contains(text(), " + str(database_name) + ")]")
  #databse_dropdown_consumer_option.click()

  create_an_order_button = driver.find_element(By.XPATH, "//input[@id='RunCounts']")
  create_an_order_button.click()
  time.sleep(1)

  #############################
  ### RUN COUNT
  #############################
  print("RUN COUNT")

  existing_radio_option = driver.find_element(By.XPATH, "//input[@type='radio'][@value='EXISTING']")
  existing_radio_option.click()

  count_name_input = driver.find_element(By.XPATH, "//input[@id='cs_Count_Name']")
  count_name_input.send_keys(count_name)

  if dedupe_type == '1PI':
    dedupe_dropdown_1pi_option = driver.find_element(By.XPATH, "//select/option[contains(text(), 'One Record Per Individual')]")
    dedupe_dropdown_1pi_option.click()
  elif dedupe_type == '1PA':
    dedupe_dropdown_1pa_option = driver.find_element(By.XPATH, "//select/option[contains(text(), 'One Record Per Household')]")
    dedupe_dropdown_1pa_option.click()
  elif dedupe_type == 'DMS':
    dedupe_dropdown_dms_option = driver.find_element(By.XPATH, "//select/option[contains(text(), 'DMS Internal Use Only')]")
    dedupe_dropdown_dms_option.click()
  else: #defaults to 1pi
    dedupe_dropdown_1pi_option = driver.find_element(By.XPATH, "//select/option[contains(text(), 'One Record Per Individual')]")
    dedupe_dropdown_1pi_option.click()

  submit_button = driver.find_element(By.XPATH, "//input[@value='Submit']")
  submit_button.click()
  time.sleep(3)

  #click submit again
  submit_button = driver.find_element(By.XPATH, "//input[@value='Submit']")
  submit_button.click()
  time.sleep(3)

  count_text = ""

  text_loaded = False
  attempt = 0
  while attempt < 5 and text_loaded == False:
    try:
      count_text = driver.find_element(By.XPATH, "//td/pre").text
      text_loaded = True
    except Exception as e:
      print(e)
      print("Not loaded, trying again...")
      time.sleep(2)
    attempt = attempt + 1

  
    if attempt >= 5 and text_loaded == False:
      input("Press enter when the page is finally done loading...")

  if text_loaded == True and count_text != "":
    count_quantity_raw_match = re.search(str(count_name) + ".*?[0-9,]+", count_text)
    count_quantity = count_quantity_raw_match.group()[len(str(count_name)):].strip()
  else:
    print("Unable to get the count quantity!")
    count_quantity = input("Please enter the count quantity here (commas are ok)...")

  #############################
  ### LOGIN TO FLASH AGAIN
  #############################
  print("LOGIN TO FLASH AGAIN")

  driver.get(flash_login_url)
  time.sleep(0.5)

  user_name_input = driver.find_element(By.XPATH, "//input[@name='username']")
  user_name_input.send_keys(flash_username)

  password_input = driver.find_element(By.XPATH, "//input[@name='password']")
  password_input.send_keys(flash_password)

  submit_button = driver.find_element(By.XPATH, "//input[@name='Login']")
  submit_button.click()
  time.sleep(0.5)

print("count_name: " + str(count_name))
print("count_quantity: " + str(count_quantity))

#############################
### SELECT CREATE ORDER
#############################
print("SELECT CREATE ORDER")

select = Select(driver.find_element(By.XPATH, "//select[@id='dbselect']"))
#databse_dropdown = driver.find_element(By.XPATH, "//select[@id='dbselect']")
#databse_dropdown.click()

select.select_by_value(str(database_dropdown_value))
#databse_dropdown_consumer_option = driver.find_element(By.XPATH, "//select[@id='dbselect']/option[contains(text(), " + str(database_name) + ")]")
#databse_dropdown_consumer_option.click()

create_an_order_button = driver.find_element(By.XPATH, "//input[@id='CreateOrder']")
create_an_order_button.click()
time.sleep(1)

#############################
### CREATE ORDER
#############################
print("CREATE ORDER")

count_quantity_clean = re.sub('[^0-9]','', count_quantity)

po_ref_input = driver.find_element(By.XPATH, "//input[@id='pofref']")
po_ref_input.send_keys(count_name)

po_ref_input = driver.find_element(By.XPATH, "//input[@id='billref']")
po_ref_input.send_keys(count_name)

row1_count_name_input = driver.find_element(By.XPATH, "//tr/td/input[@id='ocn001']")
row1_count_name_input.send_keys(count_name)

row1_qty_input = driver.find_element(By.XPATH, "//tr/td/input[@id='ocq001']")
row1_qty_input.send_keys(count_quantity_clean)

row1_nth_input = driver.find_element(By.XPATH, "//tr/td/input[@id='nthq001']")
row1_nth_input.send_keys(count_quantity_clean)

ftp_output_radio_option = driver.find_element(By.XPATH, "//td/input[@type='radio'][@value='oftp']")
ftp_output_radio_option.click()

comma_delim_radio_option = driver.find_element(By.XPATH, "//td/input[@type='radio'][@value='ocsv']")
comma_delim_radio_option.click()


if dedupe_type == '1PI':
  undup_radio_option_1pi = driver.find_element(By.XPATH, "//td/input[@type='radio'][@value='orpi']")
  undup_radio_option_1pi.click()
elif dedupe_type == '1PA':
  undup_radio_option_1pa = driver.find_element(By.XPATH, "//td/input[@type='radio'][@value='orph']")
  undup_radio_option_1pa.click()
elif dedupe_type == 'DMS':
  undup_radio_option_dms = driver.find_element(By.XPATH, "//td/input[@type='radio'][@value='tarec']")
  undup_radio_option_dms.click()
else: #defaults to 1pi
  undup_radio_option_1pi = driver.find_element(By.XPATH, "//td/input[@type='radio'][@value='orpi']")
  undup_radio_option_1pi.click()


#unselect these
state_counts_checkbox = driver.find_element(By.XPATH, "//td/input[@type='checkbox'][@name='stacounts']")
zip_counts_checkbox = driver.find_element(By.XPATH, "//td/input[@type='checkbox'][@name='pzipcounts']")
scf_counts_checkbox = driver.find_element(By.XPATH, "//td/input[@type='checkbox'][@name='scfcounts']")
county_counts_checkbox = driver.find_element(By.XPATH, "//td/input[@type='checkbox'][@name='countycounts']")

if state_counts_checkbox.is_selected() == True:
  state_counts_checkbox.click()
if zip_counts_checkbox.is_selected() == True:
  zip_counts_checkbox.click()
if scf_counts_checkbox.is_selected() == True:
  scf_counts_checkbox.click()
if county_counts_checkbox.is_selected() == True:
  county_counts_checkbox.click()
  
#############################
### SELECT FIELDS
#############################
print("SELECT FIELDS")

field_rows = driver.find_elements(By.XPATH, "//table/tbody/tr[@bgcolor='#CCCCFF']")
for field_row in field_rows:

  field_name = field_row.find_element(By.XPATH, "td[@class='style13']").text.strip()
  
  if field_name in fields_to_select: #if we want to select it, select it if itsn't or ignore if it already is
    try:
      field_checkbox = field_row.find_element(By.XPATH, "td/input[@type='checkbox']")
  
      #only clicks the checkbox if it isn't selected
      if field_checkbox.is_selected() == False:
        field_checkbox.click()
        print(str(field_name) + " selected")
      else:
        print(str(field_name) + " already selected")
    except Exception as e:
      print(e)
      input("error encountered above. exit or press enter to continue...")
  else:
    try:
      field_checkbox = field_row.find_element(By.XPATH, "td/input[@type='checkbox']")
  
      #only clicks the checkbox if it is selected
      if field_checkbox.is_selected() == True: #if we don't want to select it, unselect it if is selected or ignore if it already isn't selected
        field_checkbox.click()
        print(str(field_name) + " UN-selected")
      #else:
      #  print(str(field_name) + " already UN-selected")
    except Exception as e:
      print(e)
      input("error encountered above. exit or press enter to continue...")
  		
print("")
#input("Press enter to submit the order...")
  	
#############################
### SUBMIT ORDER
#############################
print("SUBMIT ORDER")
submit_order_button = driver.find_element(By.XPATH, "//input[@value='Submit Order']")
submit_order_button.click()
time.sleep(1)

#############################
### FINAL MESSAGES
#############################
final_message = driver.find_element(By.XPATH, "//b").text
print(final_message)
print("")

input("Exit the Window")
