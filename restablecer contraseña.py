from selenium import webdriver
import threading
from selenium.webdriver.common.keys import Keys
import time
import os

pagina=int(input("1 libreria moderna    2 ultra pc     ingrese opcion "))
browser = webdriver.Chrome("/usr/bin/chromedriver")
if pagina==1:
        #time.sleep(5)
        browser.get("https://www.libreriamoderna.es/es/registro/formReinicioClaveSolicitud.php")
        username = browser.find_element_by_name("email")
        username.send_keys("jabiera.voladora@gmail.com")
        boton=browser.find_element_by_css_selector('.btn').click()
        time.sleep(10)
        #password = browser.find_elements_by_xpath("(//input[@id='clave'])")[1].send_keys(clave)
        #password = browser.find_element_by_id("clave").send_keys(clave)
        #time.sleep(5)
elif pagina==2:
        browser.get("https://www.ultrapc.cl/my-account/lost-password/")
        #time.sleep(5)
        username = browser.find_element_by_id("user_login")
        username.send_keys("usuario")
        boton=browser.find_element_by_css_selector('.woocommerce-Button').click()
        time.sleep(10)
browser.close()