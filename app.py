#%%
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json

#%%
with open('config.json', 'r') as f:
    config = json.load(f)

USER_MAIL = config['credentials']['email']
USER_PASS = config['credentials']['password']
TIMEOUT = config['timeout']
INITIAL_SLEEP = config['initial_sleep']

def wait_presence_of_element(xpath,timeout=TIMEOUT):
    try:
        element_present = EC.presence_of_element_located((By.XPATH,xpath))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ("Timed out waiting for page to load")

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(45)

driver.get("https://prenotami.esteri.it/")
wait_presence_of_element('//*[@id="login-email"]')

email_box = driver.find_element_by_xpath('//*[@id="login-email"]')
password_box = driver.find_element_by_xpath('//*[@id="login-password"]')
email_box.send_keys(USER_MAIL)
password_box.send_keys(USER_PASS)
driver.find_element_by_xpath('//*[@id="login-form"]/button').click()

wait_presence_of_element('/html/body/main/nav/ul[1]/li[3]/a/span')
driver.find_element_by_xpath('/html/body/main/nav/ul[1]/li[3]/a/span').click()

wait_presence_of_element('//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button')
driver.find_element_by_xpath('//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button').click()

while True:
    wait_presence_of_element('//*[@id="PrivacyCheck"]')
    driver.find_element_by_xpath('//*[@id="PrivacyCheck"]').click()
    driver.find_element_by_xpath('//*[@id="btnAvanti"]').click()
    wait_presence_of_element('/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button')
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button').click()
    wait_presence_of_element('//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button')
    driver.find_element_by_xpath('//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button').click()

