import os
import time

from bs4 import BeautifulSoup
from flask import Flask
from flask import jsonify
from selenium import webdriver

FB_EMAIL = os.environ['FB_EMAIL']
FB_PASS = os.environ['FB_PASS']

if FB_EMAIL is None or FB_PASS is None:
    print('Start the script like this:')
    print('export FB_EMAIL=john.appleseed@apple.com FB_PASS=i_love_steve_jobs;python3 auto_token_generator.py')

print('FB_EMAIL =', FB_EMAIL)
print('FB_PASS =', FB_PASS)

app = Flask(__name__)


@app.route('/')
def hello_world():
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get(
        'https://www.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fexplorer%2F145634995501895%2F')
    time.sleep(3)

    # log_in_button = driver.find_element_by_class_name('_srj _srd _4jy0 _4jy3 _517h _51sy _42ft').click()
    email = driver.find_element_by_id('email')
    password = driver.find_element_by_id('pass')

    email.send_keys(FB_EMAIL)
    password.send_keys(FB_PASS)

    time.sleep(3)
    driver.find_element_by_id('loginbutton').click()
    time.sleep(3)
    # driver.find_elements_by_css_selector("[aria-controls='js_9']")[0].click()
    driver.find_element_by_css_selector("[data-intl-translation='Get Token']").click()
    time.sleep(3)
    driver.find_element_by_css_selector("[data-intl-translation='Get User Access Token']").click()
    time.sleep(3)
    driver.find_element_by_css_selector("[data-intl-translation='Get Access Token']").click()
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    token = [v for v in list(soup.find_all('input')) if
             'Paste in an existing Access Token or click' in str(v)][0].attrs['value']

    driver.quit()
    print(token)
    return jsonify({'fb_auth_token': token})


app.run()
