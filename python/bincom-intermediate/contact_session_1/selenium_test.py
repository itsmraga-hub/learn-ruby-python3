# from selenium.webdriver import Chrome

# from selenium.webdriver.chrome.options import Options

# opts = Options()
# # opts.set_headless()
# browser = Chrome(options=opts)
# browser.get('http://books.toscrape.com/')

# element = browser.find_elements(By.Name, "h3")

# print(browser)
# print(element)
# <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>

from urllib.request import urlopen
import re


url = 'http://books.toscrape.com/'

page = urlopen(url)

html = page.read()
html = html.decode("utf-8")

# pattern = r'<h3>([A-Za-z]+)</h3>'
pattern = r'<li>([A-Za-z]+)</li>'
book_names = re.findall(pattern, html)
print(book_names)