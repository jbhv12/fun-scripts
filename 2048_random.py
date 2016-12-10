from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
browser =  webdriver.Firefox()
#print(type(browser))
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')
while True:
    b=browser.find_element_by_class_name('retry-button')
    if (b.is_displayed()):
        print('over')
        b.click()
    i=random.randint(1,4)
    if i==1:
        htmlElem.send_keys(Keys.UP)
    if i==2:
        htmlElem.send_keys(Keys.DOWN)
    if i==3:
        htmlElem.send_keys(Keys.LEFT)
    if i==4:
        htmlElem.send_keys(Keys.RIGHT)

