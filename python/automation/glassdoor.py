from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os


chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome('chromedriver', options=chrome_options)

wait_time = 5

# url = "https://www.glassdoor.com/Job/software-engineering-jobs-SRCH_KO0,17.htm"

url = 'https://www.glassdoor.com/Job/index.htm'
username = 'itsragamit@gmail.com'
password = 'williamraga@123'


def scrap_jobs(job_title, job_location):
    job_input = driver.find_element(By.ID, 'searchBar-jobTitle')
    job_input.send_keys(job_title)
    location_input = driver.find_element(By.ID, 'searchBar-location')
    # print(location_input)
    location_input.send_keys(job_location)
    time.sleep(5)
    jobs = driver.find_elements(By.CLASS_NAME, 'job-title')
    driver.implicitly_wait(wait_time)
    jobs_list = []
    for job in jobs:
        jobs_list.append(job.text)

    print(jobs_list[:20])


def apply_for_job(url):
    driver.get(url)

    btn = driver.find_element(By.CLASS_NAME, 'e5tvpqr2') # Easy Apply button
    time.sleep(2)
    btn.click()

    time.sleep(3)

    driver.implicitly_wait(wait_time)
    driver.switch_to.window(driver.window_handles[-1]) 

    continue_btn = driver.find_element(By.CLASS_NAME, 'ia-continueButton')

    count = 1
    while continue_btn:
        if count == 1:
            first_name = driver.find_element("id", "input-firstName") 
            first_name.send_keys("William")
            last_name = driver.find_element("id", "input-lastName") 
            last_name.send_keys('Raga')
            country_code = driver.find_element("name", 'phoneNumberCountry')
            country_code.send_keys('KE')
            phoneNumber = driver.find_element("id", "input-phoneNumber")
            phoneNumber.send_keys(795600499)
            email = driver.find_element("id", "input-email") 
            email.send_keys('william.raga@gmail.com')
        if count == 2:
            resume_path = os.path.abspath('./tkinter.pdf')
            file_input = driver.find_element(By.ID, 'resume-upload')
            if file_input:
                file_input.send_keys(resume_path)
                print('file uploaded')
                time.sleep(10)
                driver.implicitly_wait(wait_time)

        if count == 3:
            time.sleep(5)
            understand = driver.find_element(By.XPATH, '//label[@for="input-q_10edef40754c30d24cb2cfc16ab516cc-0"]')
            understand.click()
            gender = driver.find_element(By.XPATH, '//label[@for="input-q_cc90f1913b83d255b95be0e0fea6d576-0"]')
            gender.click()
            ethnic = driver.find_element(By.NAME, 'q_c3cdeef20bc91f57d0432386866ac5b5')
            ethnic.send_keys('b')
            disability = driver.find_element(By.XPATH, '//label[@for="input-q_6d42459b4a844b1cec899083259df8e8-1"]')
            disability.click()
            veteran = driver.find_element(By.XPATH, '//label[@for="input-q_3b704f3ad4f990e41a4bcdfeeda3ebb2-1"]')
            veteran.click()
            

        continue_btn = driver.find_element(By.CLASS_NAME, 'ia-continueButton')
        continue_btn.click()
        time.sleep(1)
        count += 1


def login(url, username, password):
    driver.get(url)
    driver.implicitly_wait(wait_time)
    # button-base__button-base-module__Button
    sign_in_btn = driver.find_element(By.CLASS_NAME, 'button__button-module__Button')
    sign_in_btn.click()
    driver.implicitly_wait(wait_time)
    time.sleep(5)
    email = driver.find_element(By.ID, 'modalUserEmail')
    email.send_keys(username)
    time.sleep(2)
    btn = driver.find_element(By.NAME, 'submit')
    btn.click()
    time.sleep(3)
    _password = driver.find_element(By.ID, 'modalUserPassword')
    time.sleep(2)
    _password.send_keys(password)
    btn = driver.find_element(By.NAME, 'submit')
    btn.click()
    time.sleep(3)
    scrap_jobs('software engineer', '')


login(url='https://www.glassdoor.com/Job/index.htm', username=username, password=password)
# scrap_jobs(url)