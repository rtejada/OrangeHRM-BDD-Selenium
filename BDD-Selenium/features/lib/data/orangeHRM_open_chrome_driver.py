from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


def get_driver():

    load_dotenv(os.getcwd() + "/BDD-Selenium/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(3000)
    return driver



