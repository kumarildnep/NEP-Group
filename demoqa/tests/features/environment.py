from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):
    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--disable-infobars')
    # options.add_argument('--disable-extensions')
    # options.add_argument('--disable-notifications')

    # *** Change the chrome driver path as per the system execution ***
    context.browser = webdriver.Chrome('/Users/Name/Desktop/demoqa/chromedriver', options=options)
    context.browser.get('https://demoqa.com/login/')
    context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.quit()

