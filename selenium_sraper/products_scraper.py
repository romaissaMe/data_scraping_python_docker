import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome(executable_path='C:/Users/Lenovo/chromedriver_win32/chromedriver.exe')
driver.get('https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas')
driver.implicitly_wait(12)
links=driver.find_elements_by_class_name('product-title-link')
len(links)

#fetch data for each productavailable in the show page  by navigating to the product details page
titles=[]
prices=[]
for link in links:
    link.click()
    driver.implicitly_wait(12)
    try:
        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "shelfProductTile-title")))

        title=driver.find_element_by_class_name("shelfProductTile-title")
        price=driver.find_element_by_class_name("shelfProductTile-cupPrice")
        titles.append(title.text)
        prices.append(price)
        driver.back()
    except StaleElementReferenceException:
        print("Stale element reference exception occurred.")
        driver.back()
        driver.implicitly_wait(12)


# creating txt file
with open("iced_tea.txt", "w") as file:
    for title, price in zip(titles, prices):
        file.write(f"{title},${price}\n")