from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome('chromedriver', options=chrome_options)

url = "https://www.glassdoor.com/Job/software-engineer-jobs-SRCH_KO0,17.htm"

driver.get(url)

jobs = driver.find_elements(By.CLASS_NAME, 'job-title')

jobs_list = []
for job in jobs:
    jobs_list.append(job.text)

print(jobs_list[:20])



try:
    WebDriverWait(driver, 10).until(EC.url_contains(url))
    print("Redirected to search results page.")
except TimeoutException:
    print("Page redirect timed out.")

# # Wait for a certain number of seconds
# wait_time = 5  # Adjust the number of seconds as needed
# driver.implicitly_wait(wait_time)



