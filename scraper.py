import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
import pandas as pd

webdriver_path = 'C:/Users/shubh/Downloads/edgedriver_win64/msedgedriver.exe'  # Provide the correct path

login_url = 'https://daniel.jewelry/#/login'

load_dotenv()
password = os.getenv("PASSWORD")
number = os.getenv("NUMBER")

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

driver.get(login_url)

mobile_number_element = driver.find_element(By.XPATH, '//input[@placeholder="Mobile Number"]')
password_element = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')

mobile_number_element.send_keys(str(number))  # Assuming 'number' is the variable containing the mobile number
password_element.send_keys(password)

login_button = driver.find_element(By.CLASS_NAME, 'login_btn')
login_button.click()

time.sleep(5)

redirect_url = 'https://daniel.jewelry/#/win'
driver.get(redirect_url)

time.sleep(5)

periods = []
prices = []
numbers = []

# while True:
for i in range(124):
    # Use XPath to locate all <td> elements on the current page
    td_elements = driver.find_elements(By.XPATH, '//td')

    # Loop through all <td> elements and print their text content
    # for element in td_elements:
    #     print(element.text)
    # print(td_elements[0].text)
    # print(td_elements[1].text)
    # print(td_elements[2].text)
    # print(td_elements[3].text) ###############33
    # print(td_elements[4].text)
    # print(td_elements[5].text)
    # print(td_elements[6].text)
    # print(td_elements[7].text) ###################
    # print(td_elements[8].text)
    # print(td_elements[9].text)
    # print(td_elements[10].text)
    # print(td_elements[11].text) ###################
    # print(td_elements[12].text)
    for i in range(0, 40, 4):
        period = (td_elements[i].text)
        price = (td_elements[i + 1].text)
        number = (td_elements[i + 2].text)
        blank = (td_elements[i+4].text)


        # Append parsed data to lists
        periods.append(period)
        prices.append(price)
        numbers.append(number)

    # Find the "Next" button and click it, if available
    next_button = driver.find_elements(By.CLASS_NAME, 'van-icon-arrow')
    if next_button:
        next_button[0].click()
    else:
        # If there is no "Next" button, exit the loop
        print("Breaking the loop")
        break
    i+=1

data = {'period': periods, 'price': prices, 'number': numbers}
df = pd.DataFrame(data)

print(df)
df.to_csv('output.csv')

driver.quit()
