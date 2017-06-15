import re
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from lxml import html
from bs4 import BeautifulSoup
import time
from browsermobproxy import Server

if __name__ == '__main__':
    #url = input("Enter url of page: ")


    url = 'https://www.youtube.com/watch?v=4VwElW7SbLA'
    browser = webdriver.Chrome('/Users/chromedriver')
    browser.get(url)
    time.sleep(2)

    more_button = browser.find_element_by_id('action-panel-overflow-button')
    actions = ActionChains(browser)
    actions.move_to_element(more_button)
    time.sleep(2)
    actions.click(more_button)
    actions.perform()

    transcript_button = browser.find_element_by_xpath('//*[@id="action-panel-overflow-menu"]/li[2]/button')
    actions = ActionChains(browser)
    actions.move_to_element(transcript_button)
    time.sleep(2)
    actions.click(transcript_button)
    actions.perform()

    english_button = browser.find_element_by_xpath('//*[@id="watch-transcript-container"]/div[2]/div[1]/button')
    actions = ActionChains(browser)
    actions.move_to_element(english_button)
    time.sleep(2)
    actions.click(english_button)
    actions.perform()

    english_button2 = browser.find_element_by_xpath('//*[@id="aria-menu-id-7"]/button')
    actions = ActionChains(browser)
    actions.move_to_element(english_button2)
    time.sleep(2)
    actions.click(english_button2)
    actions.perform()


    #browser.quit()

    print(browser.page_source)




    #print(soup.prettify())
    #caption_lines = soup.find_all('div', class_='caption-line')
    #print(len(caption_lines))