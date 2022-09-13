from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def get_command(line):
    n = line.find(',')
    command = line[:n]

    if (command == "open page"):
        try:
            selector = line[n + 2:]
            driver.get(selector)
        except Exception:
            print("Page not found")

    elif (command == "find element"):
        try:
            selector = line[n + 2:]
            searchbox = driver.find_element(By.XPATH, selector)
        except Exception:
            print("element not found")

    elif (command == "find in searchline"):
        try:
            k = line.find(';')
            selector = line[n + 2:k]
            info = line[k + 3:-2]
            searchbox = driver.find_element(By.XPATH, selector)
            searchbox.send_keys(info + Keys.ENTER)
        except Exception:
            print("element not found")

    if (command == "click"):
        try:
            selector = line[n + 1:]
            button = driver.find_element(By.XPATH, selector)
            button.click()
        except Exception:
            print("button not found:   ", selector)

driver = webdriver.Chrome()

file = open('test.txt', 'r')
lines = file.readlines()

for line in lines:
    get_command(line)
file.close()
