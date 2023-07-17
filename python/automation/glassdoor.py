from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=chrome_options)


# driver.get("https://www.glassdoor.com/index.htm")
driver.get('https://www.glassdoor.com/Job/index.htm')


# job_title = driver.find_element("id", "typedKeyword-144bf2e-2611-2236-cdd8-e86c0a7de0fa") 
job_title = driver.find_element(By.NAME, "typedKeyword")
# print(job_title.__dict__)
# print(dir(job_title))
print(job_title.text)

job_title.send_keys('software engineer')

job_area = driver.find_element(By.NAME, "Autocomplete")
# job_area = driver.find_element("id", "Autocomplete-575317-b7a2-c62-a3fb-2c4a153afef")

job_title.send_keys("")

# gd-ui-button HeroSearch_searchButton__tg8_t css-24cilg e5tvpqr2
# btn = driver.find_element("class", "HeroSearch_buttonTextOverflowOverride__xNE8E")
# btn = driver.find_element(By.NAME, "clickSource")
# print(dir(btn))

btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "clickSource")))
btn.click()
# WebDriverWait(driver=driver, timeout=10).until(
#     # lambda x: x.execute_script("return document.readyState === 'complete'")
#     btn.click()
# )

# Wait for the page to redirect
url = 'https://www.glassdoor.com/Job/nairobi-software-engineer-jobs-SRCH_IL.0,7_IC2896002_KO8,25.htm?suggestCount=0&suggestChosen=false&typedKeyword=software%2520engineer&dropdown=0&Autocomplete=Nairobi&clickSource=searchBtn'

try:
    WebDriverWait(driver, 10).until(EC.url_contains(url))
    print("Redirected to search results page.")
except TimeoutException:
    print("Page redirect timed out.")

# Wait for a certain number of seconds
wait_time = 5  # Adjust the number of seconds as needed
driver.implicitly_wait(wait_time)



