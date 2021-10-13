from selenium import webdriver
import threading
from selenium.webdriver.common.keys import Keys
import time
import os

pagina=int(input("1 libreria moderna    2 ultra pc     ingrese opcion "))
browser = webdriver.Chrome("/usr/bin/chromedriver")
if pagina==1:
        browser.get("https://www.libreriamoderna.es/es/registro/autenticacion.php")
        username = browser.find_element_by_id("usuario")
        username.send_keys("bego.gordita@gmail.com")
        password = browser.find_elements_by_xpath("(//input[@id='clave'])")[1].send_keys("clavebegoña")
        time.sleep(3)
        boton=browser.find_elements_by_xpath("(//input[@type='submit'])")[1].click()
elif pagina==2:
        browser.get("https://www.ultrapc.cl/my-account")
        #time.sleep(5)
        username = browser.find_element_by_id("username")
        username.send_keys("begoña")
        password = browser.find_element_by_id("password").send_keys("clavebegoña")
        browser.find_element_by_name("login").click()
        time.sleep(5)