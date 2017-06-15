import re
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from lxml import html
from bs4 import BeautifulSoup
import time
from browsermobproxy import Server

def extract_transcript(html_page):
    caption_tags = html_page.find_all('div', class_='caption-line-text')
    caption_texts = [caption.text.lower() for caption in caption_tags]
    time_tags = html_page.find_all('div', class_='caption-line-time')
    time_texts = [time.text for time in time_tags]
    caption_time_dictionary = dict(zip(caption_texts, time_texts))
    return caption_time_dictionary

def get_caption_times(caption_time_dictionary, caption):
    times = []
    for key in caption_time_dictionary:
        if caption in key:
            times.append(caption_time_dictionary[key])
    return times


if __name__ == '__main__':
    #url = input("Enter url of page: ")

    word = input("Enter the word you're searching for: ")
    url = 'https://www.youtube.com/watch?v=4VwElW7SbLA&t=282s'
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

    time.sleep(2)

    soup = BeautifulSoup(browser.page_source, 'lxml')
    soup.prettify()
    caption_time_dictionary = extract_transcript(soup)
    times = get_caption_times(caption_time_dictionary, word)
    print(times)
