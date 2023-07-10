def main():
    from selenium.webdriver import Firefox
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options

    opts = Options()

    driver = Firefox(options=opts)

    # url = 'https://www.jobserve.com/ng/en/Job-Search/'
    url = 'https://www.jobserve.com/us/en/JobSearch.aspx?shid=FB459FE9943C20F6821E'
    driver.get(url)

    job_titles = driver.find_elements(By.CLASS_NAME, 'jobResultsTitle')

    jobs_list = []
    for job in job_titles:
        jobs_list.append(job.text)
    
    print(jobs_list[:100])


if __name__ == "__main__":
    main()
