### SET UP ###
from selenium import webdriver
from selenium.webdriver.common.by import By

profilePath = r'' #C:\Users\oscar\AppData\Roaming\Mozilla\Firefox\Profiles\...
profile = webdriver.FirefoxProfile(profilePath)

execPath = r'' #...geckodriver.exe')'
driver = webdriver.Firefox(profile, executable_path=execPath)
