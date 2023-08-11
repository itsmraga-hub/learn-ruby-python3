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

url = "https://www.glassdoor.com/Job/software-engineer-jobs-SRCH_KO0,17.htm"

driver.get(url)

# jobs = driver.find_elements(By.CLASS_NAME, 'job-title')

# jobs_list = []
# for job in jobs:
#     jobs_list.append(job.text)

# print(jobs_list[:20])

btn = driver.find_element(By.CLASS_NAME, 'e5tvpqr2')
time.sleep(2)
btn.click()

time.sleep(3)

# new_url = 'https://m5.apply.indeed.com/beta/indeedapply/form/contact-info'

# try:
    # WebDriverWait(driver, 10).until(EC.url_contains(new_url))
driver.implicitly_wait(wait_time)
driver.switch_to.window(driver.window_handles[-1]) 
# print("Redirected to apply page.")
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
        # understand = driver.find_element(By.NAME, 'input-q_10edef40754c30d24cb2cfc16ab516cc-0')
        understand = driver.find_element(By.XPATH, '//label[@for="input-q_10edef40754c30d24cb2cfc16ab516cc-0"]')
        # understand = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'input-q_10edef40754c30d24cb2cfc16ab516cc-0')))
        understand.click()
        # gender = driver.find_element(By.ID, 'input-q_cc90f1913b83d255b95be0e0fea6d576-0')
        gender = driver.find_element(By.XPATH, '//label[@for="input-q_cc90f1913b83d255b95be0e0fea6d576-0"]')
        gender.click()
        ethnic = driver.find_element(By.NAME, 'q_c3cdeef20bc91f57d0432386866ac5b5')
        # ethnic = driver.find_element(By.XPATH, '//label[@for="input-q_10edef40754c30d24cb2cfc16ab516cc-0"]')
        ethnic.send_keys('b')
        # disability = driver.find_element(By.NAME, 'input-q_6d42459b4a844b1cec899083259df8e8-1')
        disability = driver.find_element(By.XPATH, '//label[@for="input-q_6d42459b4a844b1cec899083259df8e8-1"]')
        disability.click()
        # veteran = driver.find_element(By.NAME, 'input-q_3b704f3ad4f990e41a4bcdfeeda3ebb2-1')
        veteran = driver.find_element(By.XPATH, '//label[@for="input-q_3b704f3ad4f990e41a4bcdfeeda3ebb2-1"]')
        veteran.click()
        



    continue_btn = driver.find_element(By.CLASS_NAME, 'ia-continueButton')
    continue_btn.click()
    time.sleep(1)
    count += 1
    
# except Exception:
#     print("Page redirect timed out.")

# # Wait for a certain number of seconds
# wait_time = 5  # Adjust the number of seconds as needed
# driver.implicitly_wait(wait_time)



# WebDriverWait(driver=driver, timeout=10).until(
#     lambda x: x.execute_script("return document.readyState === 'complete'")
# )
