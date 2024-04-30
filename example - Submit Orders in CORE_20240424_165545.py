print('Submit Orders in CORE_20240424_165545.py')

#DATA
script_file_name = 'Submit Orders in CORE_20240424_165545'

#SET UP DATA
_HEADER_ROW_ = 1
_FIRST_ROW_ = 3
core_login_url = 'https://coregiant.com/login/'
core_create_new_po_url = 'https://coregiant.com/po/new/id/'
core_claim_po_url = 'https://coregiant.com/po/claim/id/'
core_complete_po_url = 'https://coregiant.com/po/complete/id/'
google_sheet_id = '1bN3nhB6GRyDRj2SosTvW1SRUn1lMp3SOKrVOMKVGbwc'
username = 'oscar@giantpartners.com'
password = 'gigantic134!'
exe_path=r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver_path=r'E:\BROWSER AUTOMATION\geckodriver.exe'

#SUMMARY DATA
summary_vendor = ['B2B MOUNTAIN TOP','B2B NATIONWIDE','EMAIL OVERSIGHT','TOWER VALIDATION','CS VALIDATION','IPOST VALIDATION','WEBBULA','CS DEPLOYMENT','IPOST DEPLOYMENT','TOWER EM APPEND']

summary_type = ['USAGE','USAGE','VALIDATION','VALIDATION','VALIDATION','VALIDATION','VALIDATION','DEPLOYMENT','DEPLOYMENT','APPEND']

summary_vendor_name_in_core = ['Mountain Top Data','Nationwide Marketing Services','Email Oversight','Tower Data','CleanSender','iPost','Webbul','CleanSender','iPost','Tower Data']


#SHEET DATA
ORDER_NUMBER = [[],[],['247083','247220','247234','247213','247220','247190','247227','247189','247189','246440','247186','247212','247186','246552','246140'],['247190','246440','246140'],['247220','247213','247220'],[],[],['240865','240865','242959','242959','224661','224661','224661','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','246552','245013','245626','224661','224661','245475','224661','240865','240865'],['241003','244538','246389','246389'],[]]

QTY = [[],[],['32498','7000','7000','21000','7000','1953','1271','196160','38289','16000','108572','450','1840724','7000','134000'],['1749','14961','126762'],['6591','20330','6755'],[],[],['131456','131472','4974774','3989053','102855','103759','105264','4861','4926','4916','4911','4915','4938','4968','4804','4960','4906','4854','4927','4880','4956','4946','4923','4943','4949','4923','4949','4935','4951','4944','4836','4917','4873','4866','4930','4818','4966','4941','4945','4938','4935','4948','4959','4943','4931','4957','4889','4844','4952','4925','4874','4938','4826','4974','4953','4949','4943','4946','22308','74479','102847','103745','35463','105248','131499','131503'],['8133','65489','1282','245'],[]]

COST_PER = [[],[],['0.0007','0.0007','0.0007','0.0007','0.0007','0.0007','0.0007','0.0007','0.0007','0.0007','0.0007','0.0007','0.0007','0.0007','0.0007'],['0.001','0.001','0.001'],['0.00425','0.00425','0.00425'],[],[],['0.001','0.001','0.0008','0.0008','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001','0.001'],['0.0045','0.0007','0.0007','0.0007'],[]]

COST = [[],[],['22.75','4.9','4.9','14.7','4.9','1.37','0.89','137.31','26.8','11.2','76','0.32','1288.51','4.9','93.8'],['1.75','14.96','126.76'],['28.01','86.4','28.71'],[],[],['131.46','131.47','3979.82','3191.24','102.86','103.76','105.26','4.86','4.93','4.92','4.91','4.92','4.94','4.97','4.8','4.96','4.91','4.85','4.93','4.88','4.96','4.95','4.92','4.94','4.95','4.92','4.95','4.94','4.95','4.94','4.84','4.92','4.87','4.87','4.93','4.82','4.97','4.94','4.95','4.94','4.94','4.95','4.96','4.94','4.93','4.96','4.89','4.84','4.95','4.93','4.87','4.94','4.83','4.97','4.95','4.95','4.94','4.95','22.31','74.48','102.85','103.75','35.46','105.25','131.5','131.5'],['36.6','45.84','0.9','0.17'],[]]

PO_CHECK = [[],[],['false','false','false','false','false','false','false','false','false','false','false','false','false','false','false'],['false','false','false'],['false','false','false'],[],[],['false','false','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','true','false','false'],['false','false','false','false'],[]]

LIST_ID = [[],[],['202498','202495','202496','202494','202495','202493','202489','202468','202474','202478','202463','202459','202372','202385','202374'],['','',''],['','',''],[],[],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','',''],[]]

NAME = [[],[],['GPPO247083-1_EM_OVERSIGHT','GPPO247220_2_EMOVERSIGHT_03','GPPO247234-1_EM_OVERSIGHT','GPPO247213_2_EMOVERSIGHT','GPPO247220_2_EMOVERSIGHT','GPPO247190-1_EM_OVERSIGHT','GPPO247227-1_EM_OVERSIGHT','GPPO247186_1_ev_EM_OVERSIGHT','GPPO247186_1_STANDARD_EM_OVERSIGHT3','GPPO246440_25_EM_OVERSIGHT','GPPO247186_1_STANDARD_EM_OVERSIGHT2','GPPO247212-1_EM_OVERSIGHT','GPPO247186_1_STANDARD_EM_OVERSIGHT','GPPO246552_167_EMOVERSIGHT','GPPO246140_1_EO'],['GPPO247190-1_TOWER','GPPO246440_25_EM_tower','GPPO246140_1_TWR'],['GPPO247220_2_CS_03','GPPO247213_2_CS','GPPO247220_2_CS'],[],[],['Trailer Valet - NewData - 240865 - EM20 - A','Trailer Valet - NewData - 240865 - EM20 - B','Ethan Allen - 555555 - AprMag24 - EM2','Ethan Allen - 444444 - AprMag24 - EM2','BMW - Conquest_iX - April24 - 224661 - EM2','BMW - Conquest_i5 - April24 - 224661 - EM2','BMW - Conquest_i4 - April24 - 224661 - EM2','MINI Roadshow - MINI of Westchester - 246552 - EM2','MINI Roadshow - MINI of Ontario - 246552 - EM2','MINI Roadshow - MINI of Manhattan - 246552 - EM2','MINI Roadshow - MINI of Freeport - 246552 - EM2','MINI Roadshow - MINI of Las Vegas - 246552 - EM2','MINI Roadshow - Braman MINI of Palm Beach - 246552 - EM2','MINI Roadshow - International MINI - 246552 - EM2','MINI Roadshow - MINI of North Scottsdale - 246552 - EM2','MINI Roadshow - Orlando MINI - 246552 - EM2','MINI Roadshow - Habberstad MINI - 246552 - EM2','MINI Roadshow - MINI of Tempe - 246552 - EM2','MINI Roadshow - MINI of Glencoe North Shore - 246552 - EM2','MINI Roadshow - MINI of Ramsey - 246552 - EM2','MINI Roadshow - Tom Bush MINI - 246552 - EM2','MINI Roadshow - Patrick MINI - 246552 - EM2','MINI Roadshow - Bill Jacobs MINI - 246552 - EM2','MINI Roadshow - MINI of Charleston - 246552 - EM2','MINI Roadshow - MINI of Grand Rapids - 246552 - EM2','MINI Roadshow - MINI of Peabody - 246552 - EM1','MINI Roadshow - MINI of Bedford - 246552 - EM1','MINI Roadshow - Keeler MINI - 246552 - EM1','MINI Roadshow - MINI of Rochester - 246552 - EM1','MINI Roadshow - Herb Chambers MINI of Boston - 246552 - EM1','MINI Roadshow - MINI of Marin - 246552 - EM1','MINI Roadshow - Schomp MINI - 246552 - EM1','MINI Roadshow - MINI of Berkeley - 246552 - EM1','MINI Roadshow - MINI of Stevens Creek - 246552 - EM1','MINI Roadshow - MINI of Pensacola - 246552 - EM1','MINI Roadshow - MINI of Universal City - 246552 - EM1','MINI Roadshow - MINI of Wichita - 246552 - EM1','MINI Roadshow - Baron MINI - 246552 - EM1','MINI Roadshow - MINI of Wesley Chapel - 246552 - EM1','MINI Roadshow - MINI of Omaha - 246552 - EM1','MINI Roadshow - Ferman MINI of Tampa Bay - 246552 - EM1','MINI Roadshow - MINI of the Woodlands - 246552 - EM2','MINI Roadshow - MINI of Rochester - 246552 - EM1','MINI Roadshow - Keeler MINI - 246552 - EM1','MINI Roadshow - MINI of Peabody - 246552 - EM1','MINI Roadshow - MINI of Bedford - 246552 - EM1','MINI Roadshow - MINI of Berkeley - 246552 - EM1','MINI Roadshow - MINI of Marin - 246552 - EM1','MINI Roadshow - Herb Chambers MINI of Boston - 246552 - EM1','MINI Roadshow - Schomp MINI - 246552 - EM1','MINI Roadshow - MINI of Stevens Creek - 246552 - EM1','MINI Roadshow - MINI of Pensacola - 246552 - EM1','MINI Roadshow - MINI of Universal City - 246552 - EM1','MINI Roadshow - MINI of Wichita - 246552 - EM1','MINI Roadshow - MINI of Wesley Chapel - 246552 - EM1','MINI Roadshow - Baron MINI - 246552 - EM1','MINI Roadshow - Ferman MINI of Tampa Bay - 246552 - EM1','MINI Roadshow - MINI of Omaha - 246552 - EM1','UofL Health - 245013 - EM2 (retargeting)','Media Farm (SAWEP) - 245626 - EM4','BMW - Conquest_iX - April24 - 224661 - EM1','BMW - Conquest_i5 - April24 - 224661 - EM1','The Ultimate Gun Show - 245475 - EM4','BMW - Conquest_i4 - April24 - 224661 - EM1','Trailer Valet - NewData - 240865 - EM19 - A','Trailer Valet - NewData - 240865 - EM19 - B'],['Military Connect - 241003 - EM1v5 - DAY85','Giant Partners - 244538 - EM12 - DAY3','Gerety Orthodontic Seminars - 246389 - B2C - EM2 - DAY8','Gerety Orthodontic Seminars - 246389 - B2B - EM2 - DAY8'],[]]

FULL_PO = [[],[],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_'],['_','_','_'],[],[],['_','_','242959-20','242959-21','224661-380','224661-381','224661-382','246552-133','246552-134','246552-135','246552-136','246552-137','246552-138','246552-139','246552-140','246552-141','246552-142','246552-143','246552-144','246552-145','246552-146','246552-147','246552-148','246552-149','246552-150','246552-151','246552-152','246552-153','246552-154','246552-155','246552-156','246552-157','246552-158','246552-159','246552-160','246552-161','246552-162','246552-163','246552-164','246552-165','246552-166','246552-116','246552-117','246552-118','246552-119','246552-120','246552-121','246552-122','246552-123','246552-124','246552-125','246552-126','246552-127','246552-128','246552-129','246552-130','246552-131','246552-132','245013-9','245626-9','224661-377','224661-378','245475-11','224661-379','_','_'],['_','_','_','_'],[]]

PO_LINK = [[],[],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_'],['_','_','_'],[],[],['_','_','https://coregiant.com/po/view/id/77508','https://coregiant.com/po/view/id/77509','https://coregiant.com/po/view/id/77510','https://coregiant.com/po/view/id/77511','https://coregiant.com/po/view/id/77512','https://coregiant.com/po/view/id/77513','https://coregiant.com/po/view/id/77514','https://coregiant.com/po/view/id/77515','https://coregiant.com/po/view/id/77516','https://coregiant.com/po/view/id/77517','https://coregiant.com/po/view/id/77518','https://coregiant.com/po/view/id/77519','https://coregiant.com/po/view/id/77520','https://coregiant.com/po/view/id/77521','https://coregiant.com/po/view/id/77522','https://coregiant.com/po/view/id/77523','https://coregiant.com/po/view/id/77524','https://coregiant.com/po/view/id/77525','https://coregiant.com/po/view/id/77526','https://coregiant.com/po/view/id/77527','https://coregiant.com/po/view/id/77528','https://coregiant.com/po/view/id/77529','https://coregiant.com/po/view/id/77530','https://coregiant.com/po/view/id/77531','https://coregiant.com/po/view/id/77532','https://coregiant.com/po/view/id/77533','https://coregiant.com/po/view/id/77534','https://coregiant.com/po/view/id/77535','https://coregiant.com/po/view/id/77536','https://coregiant.com/po/view/id/77537','https://coregiant.com/po/view/id/77538','https://coregiant.com/po/view/id/77539','https://coregiant.com/po/view/id/77540','https://coregiant.com/po/view/id/77541','https://coregiant.com/po/view/id/77542','https://coregiant.com/po/view/id/77544','https://coregiant.com/po/view/id/77546','https://coregiant.com/po/view/id/77547','https://coregiant.com/po/view/id/77548','https://coregiant.com/po/view/id/77315','https://coregiant.com/po/view/id/77316','https://coregiant.com/po/view/id/77317','https://coregiant.com/po/view/id/77318','https://coregiant.com/po/view/id/77319','https://coregiant.com/po/view/id/77320','https://coregiant.com/po/view/id/77321','https://coregiant.com/po/view/id/77322','https://coregiant.com/po/view/id/77323','https://coregiant.com/po/view/id/77324','https://coregiant.com/po/view/id/77325','https://coregiant.com/po/view/id/77326','https://coregiant.com/po/view/id/77327','https://coregiant.com/po/view/id/77328','https://coregiant.com/po/view/id/77329','https://coregiant.com/po/view/id/77330','https://coregiant.com/po/view/id/77331','https://coregiant.com/po/view/id/77332','https://coregiant.com/po/view/id/77333','https://coregiant.com/po/view/id/77334','https://coregiant.com/po/view/id/77335','https://coregiant.com/po/view/id/77336','https://coregiant.com/po/view/id/77337','_','_'],['_','_','_','_'],[]]

first_row_index_per_sheet = [0,0,7,12,11,0,0,28,10,0]

lowest_row_index_per_sheet = [0,0,21,14,13,0,0,93,13,0]

po_check_col_index_per_sheet = [6,6,15,15,14,12,13,8,9,13]

full_oc_col_index_per_sheet = [7,7,17,17,15,13,14,9,10,14]

core_link_col_index_per_sheet = [8,8,18,18,16,14,15,10,11,15]

qty_col_index_per_sheet = [3,3,5,5,4,4,4,3,4,10]


#------------------------
# SET UP PYTHON
#------------------------
print("Setting Up...")

import os
import time

#FOR SELENIUM
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By #for selenium’s find_element

#FOR GOOGLE SHEETS API
import os.path
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

options = Options()
options.binary_location = exe_path
service = Service(driver_path)
driver = webdriver.Firefox(service=service, options=options)

#------------------------
# CREATE OUTPUT FILE
#------------------------
#print("Creating Output File...")
#output_file_path = os.getcwd() + r'\\' + script_file_name + '.csv' #CURRENT DIRECTORY + #NAMED CSV FILE
#output_file = open(output_file_path, "a")
#output_file.write('"OC","FULL ORDER NUMBER","CORE LINK","CORE ID","PRODUCT #DETAILS","QTY","COST PER","DATE TIME CREATED"\n')

#------------------------
# PASS WEBROOT
#------------------------
print("Passing Webroot...")
try:
    allow_button = driver.find_element(By.XPATH, "//input[@id='allowButton']")
    allow_button.click()
except:
    pass

#------------------------
# LOGIN TO CORE
#------------------------
print("Logging in to Core...")

driver.get(core_login_url)
time.sleep(2)

username_text_field = driver.find_element(By.XPATH, "//input[@id='email']")
username_text_field.send_keys(username)

password_text_field = driver.find_element(By.XPATH, "//input[@id='pswd']")
password_text_field.send_keys(password)

log_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
log_in_button.click()
time.sleep(2)

#------------------------
# LOOP THROUGH EACH VENDOR / SHEET AND CREATE POs IN CORE
#------------------------
print("")

print("-----------------------------------------------")
print("Creating POs")
print("-----------------------------------------------")
print("")

#things to update in google sheet
updated_po_check = []
updated_full_oc = []
updated_core_link = []
orders_created = 0

try:
 v = 0
 while v < len(summary_vendor):

  vendor = summary_vendor[v]
  order_type = summary_type[v]
  vendor_name_in_core = summary_vendor_name_in_core[v]
  
  updated_po_check.append([])
  updated_full_oc.append([])
  updated_core_link.append([])
  
  #COUNTING NUMBER OF VALID ORDERS TO SUBMIT (not necessary but helps make the output window a little more clear)
  i = 0
  number_of_orders = len(ORDER_NUMBER[v])
  number_of_potentially_valid_orders = 0
  i_valid = 0
  is_i_valid = False
  
  while i < number_of_orders:
    oc_number = ORDER_NUMBER[v][i]
    po_check = PO_CHECK[v][i]
    qty = QTY[v][i] 
    
    if str(oc_number) == "" or str(oc_number) == '-': #or elif str(oc_number).isdigit() == False or len(str(oc_number)) != 6:
      pass
    elif po_check == 'true':
      pass
    elif str(qty) == '0' or str(qty) == 'undefined' or str(qty) == '' or str(qty) == '-': 
      pass
    else:
      number_of_potentially_valid_orders = number_of_potentially_valid_orders + 1
    i = i + 1
    
  print(str(vendor) + "... " + str(number_of_potentially_valid_orders) + " POs found.")
  
  
  i = 0
  while i < number_of_orders:
      
    is_i_valid = False
    
    oc_number = ORDER_NUMBER[v][i]
    qty = QTY[v][i] 
    cost_per = COST_PER[v][i]
    cost = COST[v][i]
    po_check = PO_CHECK[v][i]
    list_id = LIST_ID[v][i]
    name = NAME[v][i]
    
    item = "1"
    
    full_oc = "_"
    core_link = "_"
    core_id = ""
    po_created = False

    if str(oc_number) == "" or str(oc_number) == "-": #SKIP and no print
      pass
    elif po_check == 'true': #SKIP and no print
      pass
    elif str(qty) == '0' or str(qty) == 'undefined' or str(qty) == '' or str(qty) == '-': #SKIP and no print
      pass
  
    elif str(oc_number).isdigit() == False or len(str(oc_number)) != 6:

      print(str(i_valid + 1) + " / " + str(number_of_potentially_valid_orders) + ": " + str(name) + " " + str(oc_number) + " skipped because ORDER NUMBER or QTY is invalid, or already submmitted.")
      is_i_valid = True
      
    else: #DON'T SKIP
    
      print(str(i_valid + 1) + " / " + str(number_of_potentially_valid_orders) + ": " + str(name) + " " + str(oc_number) + " (" + f'{int(qty):,}' + " at $" + str(cost_per) + " = $" + str(cost) + ")")
      is_i_valid = True
      
      driver.get(str(core_create_new_po_url) + str(oc_number))
      time.sleep(1)
      
      #with-in the add-more pop-up
      could_create_po = False
      try:
        add_more_button = driver.find_element(By.XPATH, "//button[@class='btn btn-secondary btn-xs add']")
        add_more_button.click()
        could_create_po = True
      except:
      	print("COULD NOT CREATE NEW PO, SKIPPED!")
      	could_create_po = False
      	
      if could_create_po == True:
        item_text_field = driver.find_element(By.XPATH, "//input[@id='item']")
        item_text_field.send_keys(item)

        desc_text_field = driver.find_element(By.XPATH, "//input[@id='description']")
        desc_text_field.send_keys(order_type)

        qty_text_field = driver.find_element(By.XPATH, "//input[@id='quantity']")
        qty_text_field.send_keys(qty)

        price_text_field = driver.find_element(By.XPATH, "//input[@id='price']")
        price_text_field.send_keys(cost_per)

        product_details_textarea = driver.find_element(By.XPATH, "//textarea[@id='details']")
    
        if name == '' or name == 'undefined':
          product_details_textarea.send_keys(str(oc_number))
        else:
          product_details_textarea.send_keys(str(name))
   
        save_line_item_button = driver.find_element(By.XPATH, "//button[@id='save-product']")
        save_line_item_button.click()
        
        notes_text_area = driver.find_element(By.XPATH, "//textarea[@name='notes']")
        notes_text_area.clear() #this may not work, may need to send CTRL+A then DEL (if yes then make sure to import relevant library at the top)
        
        #adding the vendor
        vendor_dropdown = driver.find_element(By.XPATH, "//select[@name='vendor']")
        vendor_dropdown.click()
        vendor_dropdown.send_keys(vendor_name_in_core)
        time.sleep(0.1)
        
        #submit
        save_final_button = driver.find_element(By.XPATH, "//button[@type='submit'][contains(text(),'Save')]")
        save_final_button.click()
        time.sleep(2)
    
        #submit POs
        core_link = ""
        full_oc = ""
        core_id = ""
        
        do_it_again = True
        while do_it_again == True:
          try:
            core_link = driver.current_url
            full_oc = driver.find_element(By.XPATH, "//h2[@class='font-light text-white']").text
            #needs to get the core_id and not the po number
            #need to test to make sure this works 100% of the time, now it only works ~95% of the time
            core_link_split = core_link.split("/")
            core_id = core_link_split[len(core_link_split) - 1]
            do_it_again = False
          except Exception as e:
            print(e)
            do_it_again_input = input("Enter n to just move on. Enter anything else to try again.")
            if do_it_again_input == 'n':
              do_it_again = False
              
        driver.get(str(core_complete_po_url) + str(core_id))
        time.sleep(1)
        
        notes_text_area = driver.find_element(By.XPATH, "//textarea[@name='notes']")
        notes_text_area.clear() #this may not work, may need to send CTRL+A then DEL (if yes then make sure to import relevant library at the top)
        complete_po_save_button = driver.find_element(By.XPATH, "//div[@class='card-footer']/button")
        complete_po_save_button.click()
        time.sleep(1)

        #IF CORE_ID IS SAME AS OC NUMBER THEN MOST LIKELY:
        #ORDER WAS CREATED BUT NOT COMPLETED
        #WHEN GOOGLE SHEET IS UPDATED, TELL USER SOMETHING IS WRONG
        if str(core_id) == str(oc_number):
          po_created = False  
          full_oc = "ORDER LIKELY CREATED BUT NOT COMPLETED, PLEASE CHECK IN CORE!"
          core_link = "ORDER LIKELY CREATED BUT NOT COMPLETED, PLEASE CHECK IN CORE!"
        else:
          po_created = True  

        orders_created = orders_created + 1
      
    #append to update lists
    updated_po_check[v].append([po_created])
    updated_full_oc[v].append([str(full_oc)])
    updated_core_link[v].append([str(core_link)])
    
    if is_i_valid == True:
      i_valid = i_valid + 1
      
    i = i + 1
    
  print("")  
  
  v = v + 1
except Exception as e:
 print("SUBMITTED IN CORE:")
 print(updated_po_check)
 print(updated_full_oc)
 print(updated_core_link)
 print("")
 print(e)
 input("Enter to move on and let the script update the spreadsheet with the above printed data. Or copy/paste the above data to manually update the spreadsheet yourself then exit this window.")
 
print(str(orders_created) + " POs created in total")
#print(str(orders_created) + " POs created in total, review them in the output file at this path: " + str(output_file_path))
print("")

#continue_to_update_sheet = input("Enter q to quit, or enter anything else to let the script update the Google Sheet   -->   https://docs.google.com/spreadsheets/d/" + str(google_sheet_id))
#print("")
#if continue_to_update_sheet == 'q':
#  input("Exit the window.")
#  exit()

#------------------------
# UPDATE THE GOOGLE SHEET
#------------------------
print("-----------------------------------------------")
print("Updating the Google Spreadsheet")
print("-----------------------------------------------")
print("")

#CONNECT TO GOOGLE SHEETS API
print("Connecting to Google Sheets API...\nPlese make sure credentials.json is in the same directory as this script.\nIf this your first running this script, you will need to follow the prompt to authorize use of the API.")
print("")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = None
if os.path.exists("token.json"):
  creds = Credentials.from_authorized_user_file("token.json", SCOPES)
if not creds or not creds.valid:
  if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())
  else:
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)
  with open("token.json", "w") as token:
    token.write(creds.to_json())
service = build("sheets", "v4", credentials=creds)

#LOOP THROUGH EACH SHEET / VENDOR, UPDATE AS NEEDED
v = 0
while v < len(summary_vendor):
  vendor = summary_vendor[v]
  order_type = summary_type[v]
  vendor_name_in_core = summary_vendor_name_in_core[v]

  print("Updating " + str(len(updated_po_check[v])) + " orders in sheet " + str(vendor) + "... ")
    
  if(len(updated_po_check[v]) > 0):
      
    #get google sheet values
    sheet = service.spreadsheets()
    get_range = "'" + str(vendor) + "'!A" + str(first_row_index_per_sheet[v]) + ":Z" + str(lowest_row_index_per_sheet[v])
    result = sheet.values().get(spreadsheetId = str(google_sheet_id), range=str(get_range)).execute()
    values = result.get("values", [])

    ##########################################################
    # update po check
    ##########################################################
    try:
      print("Updating PO CHECK...")
      if len(po_check_col_index_per_sheet) > 0:
        po_check_col_index = po_check_col_index_per_sheet[v]
        if po_check_col_index >= 1:
        
          po_check_update_values = updated_po_check[v]
          po_check_col_alpha = chr(65 + po_check_col_index - 1)
      
          #only allow py to overwrite data in pocheck if it's 'FALSE'
          p = 0
          while p < len(updated_po_check[v]):
            if values[p][po_check_col_index - 1] != 'FALSE':
              po_check_update_values[p][0] = values[p][po_check_col_index - 1]
            p = p + 1
      
          body = {"values": po_check_update_values}
          update_range = "'" + str(vendor) + "'!" + str(po_check_col_alpha) + str(first_row_index_per_sheet[v]) + ":" + str(po_check_col_alpha) + str(lowest_row_index_per_sheet[v])
          result = service.spreadsheets().values().update(spreadsheetId = str(google_sheet_id), range=str(update_range), valueInputOption="USER_ENTERED", body=body,).execute()
    except:
      print("UNABLE TO UPDATE PO CHECK! Moving on...")
      
    ##########################################################
    # update full oc
    ##########################################################
    try:
      print("Updating FULL PO...")
      if len(full_oc_col_index_per_sheet) > 0:
        full_oc_col_index = full_oc_col_index_per_sheet[v]
        if full_oc_col_index >= 1:
    
          full_oc_update_values = updated_full_oc[v]
          full_oc_col_alpha = chr(65 + full_oc_col_index - 1)
      
          #only allow py to overwrite data in fulloc if it's "_"
          p = 0
          while p < len(updated_full_oc[v]):
            if str(values[p][full_oc_col_index - 1]) != "_":
              full_oc_update_values[p][0] = values[p][full_oc_col_index - 1]
            p = p + 1
      
          body = {"values": full_oc_update_values}
          update_range = "'" + str(vendor) + "'!" + str(full_oc_col_alpha) + str(first_row_index_per_sheet[v]) + ":" + str(full_oc_col_alpha) + str(lowest_row_index_per_sheet[v])
          result = service.spreadsheets().values().update(spreadsheetId = str(google_sheet_id), range=str(update_range), valueInputOption="USER_ENTERED", body=body,).execute()
    except:
      print("UNABLE TO UPDATE FULL PO! Moving on...")
      
    ##########################################################
    # update core link
    ##########################################################
    try:
      print("Updating PO LINK...")
      if len(core_link_col_index_per_sheet) > 0:
        core_link_index = core_link_col_index_per_sheet[v]
        if core_link_index >= 1:
    
          core_link_update_values = updated_core_link[v]
          core_link_col_alpha = chr(65 + core_link_index - 1)
      
          #only allow py to overwrite data in corelink if it's "_"
          p = 0
          while p < len(updated_core_link[v]):
            if str(values[p][core_link_index - 1]) != "_":
              core_link_update_values[p][0] = values[p][core_link_index - 1]
            p = p + 1
      
          body = {"values": core_link_update_values}
          update_range = "'" + str(vendor) + "'!" + str(core_link_col_alpha) + str(first_row_index_per_sheet[v]) + ":" + str(core_link_col_alpha) + str(lowest_row_index_per_sheet[v])
          result = service.spreadsheets().values().update(spreadsheetId = str(google_sheet_id), range=str(update_range), valueInputOption="USER_ENTERED", body=body,).execute()
    except:
      print("UNABLE TO UPDATE PO LINK! Moving on...")
  
  print("")
  v = v + 1

input("Exit the window.")



