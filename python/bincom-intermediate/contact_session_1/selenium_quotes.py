def main():
    from selenium.webdriver import Firefox
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options

    opts = Options()

    driver = Firefox(options=opts)

    url = 'http://quotes.toscrape.com'
    driver.get(url)

    books = driver.find_elements(By.CLASS_NAME, 'text')

    books_list = []
    for book in books:
        books_list.append(book.text)
    
    print(books_list[:20])


if __name__ == "__main__":
    main()
