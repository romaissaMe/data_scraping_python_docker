from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/Users/Lenovo/chromedriver_win32/chromedriver.exe')
driver.get('https://www.woolworths.com.au/shop/browse/fruit-veg')
driver.implicitly_wait(10)
#extract products
products=driver.find_elements(By.CLASS_NAME, "product-tile-title")

Prd=[]
for product in products:
    Prd.append(product.text)

#extract corresponding prices
prices=driver.find_elements(By.CLASS_NAME, "primary")
Pr=[]
for price in prices:
    Pr.append(price.text)

# creating txt file
with open("fruit_veg.txt", "w") as file:
    for title, price in zip(Prd, Pr):
        file.write(f"{title},${price}\n")