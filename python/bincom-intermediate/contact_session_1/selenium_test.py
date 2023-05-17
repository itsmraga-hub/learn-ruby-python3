def main():
    from selenium.webdriver import Firefox
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options

    opts = Options()

    driver = Firefox(options=opts)

    url = 'http://books.toscrape.com'
    driver.get(url)

    books = driver.find_elements(By.TAG_NAME, 'h3')

    books_list = []
    for book in books:
        books_list.append(book.text)


if __name__ == "__main__":
    main()
