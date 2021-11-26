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
mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 1000, "pixelRatio": 1.4 },
    }

firefox_options = webdriver.ChromeOptions()
firefox_options.add_argument('--no-sandbox')
firefox_options.headless = True
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

def action_change():
    browser.get("https://m.youtube.com/")
    sleep(5)
    print(f"[*] Trying Use Channel")
    wait(browser,50).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytm-app/ytm-mobile-topbar-renderer/header/div/ytm-topbar-menu-button-renderer/button'))).click()
    sleep(1.5)
    xpath_el('//div[@aria-label="Ganti akun"]')

def action_change_web():
    sleep(3)
    xpath_el('//button[@id="avatar-btn"]')
    sleep(1)
    try:
        xpath_el('//yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[4]/a/tp-yt-paper-item/yt-icon')
    except:
        xpath_el('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[4]/a/tp-yt-paper-item')
def menu_comment(i):
    i = i.split("|")
    email = i[0]
    password = i[1]
    global browser
    firefox_options.add_argument('--incognito')
    firefox_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.20 Safari/537.36")
    firefox_options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(options=firefox_options)
    browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    print("[*] Trying to Login")
    login(email,password)
    global channel_name
    action_change()
    sleep(1.5)
    global get_comment
    multi_acc = wait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH, '(//div[@class="account-item-content"])')))
    comment_file = "comment.txt"
    comment_get = open(f"{cwd}/{comment_file}","r")
    get_comment = myfile.read()
    for i in range(1,len(multi_acc)+1):
        channel_name = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'(/html/body/div[2]/div/ytm-multi-page-menu-renderer/div/ytm-account-section-list-renderer/div/button/ytm-account-item-renderer/div/div/div/div[1])[{i}]'))).text
        sleep(1.5)
        xpath_el(f'(//div[@class="account-item-content"])[{i}]')
        print(f"[*] [{channel_name}] Switch Channel")
      
        print(f"[*] [{channel_name}] Trying to Comment")
        try:
            yt_comment(i)
        except:
            pass
        try:
            action_change()
        except:
            pass
def yt_report(i):
    
    print(f"[*] [{channel_name}] Trying to Report")
    browser.save_screenshot("SCROLL_DOWN.png")
    try:
        scroll_down = wait(browser,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/h1/yt-formatted-string')))
        browser.execute_script("arguments[0].scrollIntoView();", scroll_down)
        
    except:
        browser.save_screenshot("errror_headles.png")
   
      
    while True:
    
        try:
            browser.execute_script("window.scrollTo(0, 1080)")
            sleep(10)
            target_report = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '(//ytd-comment-renderer/div[3]/div[2]/ytd-comment-action-buttons-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-icon-button)[1]')))
            break
        except:
            browser.save_screenshot("errror_headles6.png")
     
    target_name = wait(browser,60).until(EC.presence_of_element_located((By.XPATH, '//a/ytd-channel-name/div/div/yt-formatted-string'))).text
    target_report.click()
    
    print(f"[*] [{channel_name}] Found Comment from [{target_name}]")
    xpath_el('//ytd-menu-service-item-renderer[@class="style-scope ytd-menu-popup-renderer iron-selected"]')
    sleep(2)
    xpath_el('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/tp-yt-paper-dialog-scrollable/div/div/yt-options-renderer/div/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]/div[1]')
    sleep(2)
    xpath_el('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/div/yt-button-renderer[2]/a/tp-yt-paper-button')
    print(f"[*] [{channel_name}] Report Successfully")
    sleep(2)
    xpath_el('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog[2]/yt-confirm-dialog-renderer/div[2]/div/yt-button-renderer[2]/a/tp-yt-paper-button/yt-formatted-string')

def yt_like(i):
    
    print(f"[*] [{channel_name}] Trying to Like")
    # browser.save_screenshot("SCROLL_DOWN.png")
    try:
        scroll_down = wait(browser,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/h1/yt-formatted-string')))
        browser.execute_script("arguments[0].scrollIntoView();", scroll_down)
        
    except:
        browser.save_screenshot("errror_headles.png")
   
    
    while True:
    
        try:
            browser.execute_script("window.scrollTo(0, 1080)")
            sleep(10)
            target_report = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '(//ytd-comment-renderer/div[3]/div[2]/ytd-comment-action-buttons-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-icon-button)[1]')))
            break
        except:
             
        
            browser.save_screenshot("errror_headles6.png")
     
    target_name = wait(browser,60).until(EC.presence_of_element_located((By.XPATH, '//a/ytd-channel-name/div/div/yt-formatted-string'))).text
 
    print(f"[*] [{channel_name}] Found Comment from [{target_name}]")
 
    
    sleep(2)
    xpath_el('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[1]/ytd-comment-renderer/div[3]/div[2]/ytd-comment-action-buttons-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-icon-button/button')
    print(f"[*] [{channel_name}] Like Successfully")

def menu_like(i):
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
    browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "platform":"Windows"})
    
    browser.execute_script(f"window.open('{targeturl}');")
    browser.switch_to.window(browser.window_handles[1])
    sleep(0.5)
    browser.close()
    sleep(1)
    try:
        browser.switch_to.window(browser.window_handles[0])
    except:
        pass
    browser.get(targeturl)
    sleep(1)
    browser.get(targeturl)
    sleep(1)
    action_change_web()
    multi_acc = wait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH, '//tp-yt-paper-icon-item[@class="style-scope ytd-account-item-renderer"]')))
    
    for i in range(1, len(multi_acc)+1):
        channel_name = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'(//yt-formatted-string[@id="channel-title"])[{i}]'))).text
        wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'(//tp-yt-paper-icon-item[@class="style-scope ytd-account-item-renderer"])[{i}]'))).click()
        
        print(f"[*] [{channel_name}] Switch Channel")
        try:
            yt_like(i)
        except:
            pass
        try:
            action_change_web()
        except:
            pass


def menu_report(i):
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
    browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "platform":"Windows"})
    
    browser.execute_script(f"window.open('{targeturl}');")
    browser.switch_to.window(browser.window_handles[1])
    sleep(0.5)
    browser.close()
    sleep(1)
    try:
        browser.switch_to.window(browser.window_handles[0])
    except:
        pass
    browser.get(targeturl)
    sleep(1)
    browser.get(targeturl)
    sleep(1)
    action_change_web()
    multi_acc = wait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH, '//tp-yt-paper-icon-item[@class="style-scope ytd-account-item-renderer"]')))
    
    for i in range(1, len(multi_acc)+1):
        channel_name = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'(//yt-formatted-string[@id="channel-title"])[{i}]'))).text
        wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'(//tp-yt-paper-icon-item[@class="style-scope ytd-account-item-renderer"])[{i}]'))).click()
        
        print(f"[*] [{channel_name}] Switch Channel")
        try:
            yt_report(i)
        except:
            pass
        try:
            action_change_web()
        except:
            pass

def yt_comment(i):
    sleep(3)
    
    browser.get(targeturl)
    print(f"[*] [{channel_name}] Trying to Comment")
    wait(browser,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.page-container > ytm-watch > ytm-single-column-watch-next-results-renderer > ytm-item-section-renderer:nth-child(3) > lazy-list > ytm-comments-entry-point-header-renderer > button'))).click()
    wait(browser,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.page-container > ytm-watch > ytm-engagement-panel > ytm-engagement-panel-section-list-renderer > div > div > div.engagement-panel-content-wrapper > ytm-section-list-renderer > lazy-list > ytm-item-section-renderer > ytm-comments-header-renderer > ytm-comment-simplebox-renderer > div'))).click()
    input_comment = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//textarea[@class="comment-simplebox-reply"]')))
    input_comment.send_keys(get_comment)
    wait(browser,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.page-container > ytm-watch > ytm-engagement-panel > ytm-engagement-panel-section-list-renderer > div > div > div.engagement-panel-content-wrapper > ytm-section-list-renderer > lazy-list > ytm-item-section-renderer > ytm-comments-header-renderer > ytm-comment-simplebox-renderer > div > div > c3-material-button:nth-child(2) > button'))).click()
    sleep(2)
    print(f"[*] [{channel_name}] Comment Successfully")
    
    
def login(email, password):
        
    global element
    global browser

    sleep(3)

    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))).send_keys(email)
    browser.find_element(By.XPATH,'//input[@type="email"]').send_keys(Keys.ENTER)

    sleep(2)

    try:
        element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        element.click()
        element.send_keys(password)
        element.send_keys(Keys.ENTER)
    except:
        browser.refresh()

        element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        element.click()
        element.send_keys(password)
        element.send_keys(Keys.ENTER)
    sleep(5)
    

if __name__ == '__main__':
    global list_accountsplit
    global k
    global targeturl
    global choice
    global nama_target
    nama_target = "mone moner"
    print("[*] Youtube Tool")
    print("[*] Don't Share to Anybody or Sell!")
    file_list = "email_akun.txt"
    myfile = open(f"{cwd}/{file_list}","r")
    list_account = myfile.read()
    list_accountsplit = list_account.split("\n")
    k = list_accountsplit
    print("[*] Menu")
    print("[*] 1. Auto Comment.")
    print("[*] 2. Auto Like Comment.")
    print("[*] 3. Auto Report Comment.")
    pilihan = int(input("[*] Masukan Pilihan (1/2/3): "))
    targeturl = input("[*] Input Target URL: ")
    if pilihan == 1:
        for i in k:
            try:
                menu_comment(i)
                try:
                    browser.quit()
                except:
                    pass
            except:
                try:
                    browser.quit()
                    pass
                except:
                    pass
       
    elif pilihan == 2:
        for i in k:
            try:
                menu_like(i)
                try:
                    browser.quit()
                except:
                    pass
            except:
                try:
                    browser.quit()
                    pass
                except:
                    pass
    elif pilihan == 3:
        for i in k:
            try:
                menu_report(i)
                try:
                    browser.quit()
                    pass
                except:
                    pass
            except:
                try:
                    browser.quit()
                    pass
                except:
                    pass
                

       
    
