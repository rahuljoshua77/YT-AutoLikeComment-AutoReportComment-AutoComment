import undetected_chromedriver as uc
uc.install()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re 
import os

cwd = os.getcwd()


firefox_options = webdriver.ChromeOptions()
firefox_options.add_argument('--no-sandbox')
firefox_options.headless = False
firefox_options.add_argument('--disable-setuid-sandbox')
firefox_options.add_argument('disable-infobars')
firefox_options.add_argument('--ignore-certifcate-errors')
firefox_options.add_argument('--ignore-certifcate-errors-spki-list')
#firefox_options.add_argument('--disable-accelerated-2d-canvas')
firefox_options.add_argument('--no-zygote')
firefox_options.add_argument('--no-first-run')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument("--disable-infobars")
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--disable-popup-blocking")
firefox_options.add_argument('--log-level=3') 
firefox_options.add_argument('--disable-blink-features=AutomationControlled')
firefox_options.add_experimental_option("useAutomationExtension", False)
firefox_options.add_experimental_option("excludeSwitches",["enable-automation"])
firefox_options.add_experimental_option('excludeSwitches', ['enable-logging'])
firefox_options.add_argument('--disable-notifications')

firefox_options.add_argument("--mute-audio")

def xpath_el(el):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el))).click()

def open_browser(i):
    i = i.split("|")
    email = i[0]
    password = i[1]
    sleep(3)
    global browser
    global channel_name
    firefox_options.add_argument('--incognito')
    firefox_options.add_argument("--window-size=1980,1020")
    firefox_options.add_argument('--start-maximized')
    firefox_options.add_argument(f"user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/{random.randint(100,800)}.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/{random.randint(100,800)}.{random.randint(10,99)}")
    browser = webdriver.Chrome(options=firefox_options)
    browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    print("[*] Trying to Login")
    login(email,password)
    
def login(email, password):
        
    global element
    global browser

    sleep(3)
    #browser.save_screenshot("commeng_log.png")
    try:
        wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))).send_keys(email)
        #browser.save_screenshot("commeng_email.png")
        browser.find_element(By.XPATH,'//input[@type="email"]').send_keys(Keys.ENTER)
    except:
        browser.save_screenshot("commeng_log_err.png")
        print("errr")
    sleep(2)

    try:
        element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        element.click()
        #browser.save_screenshot("commeng_pass_1.png")
        element.send_keys(password)
        #browser.save_screenshot("commeng_pass_2.png")
        element.send_keys(Keys.ENTER)
        #browser.save_screenshot("commeng_pass_3.png")
    except:
        browser.refresh()

        element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        element.click()
        element.send_keys(password)
        element.send_keys(Keys.ENTER)
    
    sleep(5)
    next = input("[*] Enter for Next account: ")
    browser.quit()
if __name__ == '__main__':
    global list_accountsplit
    global k
    global targeturl
    global choice
    global nama_target
    
    print("[*] Youtube Login")
    print("[*] Don't Share to Anybody or Sell!")
    file_list = "email_akun.txt"
    myfile = open(f"{cwd}/{file_list}","r")
    list_account = myfile.read()
    list_accountsplit = list_account.split("\n")
    k = list_accountsplit
    for i in k:
        try:
            open_browser(i)
        except:
            try:
                browser.quit()
            except:
                pass
      
