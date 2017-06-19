import sys
import requests
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

WAIT_TIME = 10

def extract_transcript(html_page):
    caption_tags = html_page.find_all('div', class_='caption-line-text')
    caption_texts = [caption.text.lower() for caption in caption_tags]
    time_tags = html_page.find_all('div', class_='caption-line-time')
    time_texts = [time.text for time in time_tags]
    caption_time_dictionary = dict(zip(caption_texts, time_texts))
    return caption_time_dictionary

def get_caption_times(caption_time_dictionary, target):
    times = []
    for key in caption_time_dictionary:
        if target in key:
            times.append(caption_time_dictionary[key])
    return times

def open_transcript():
    time.sleep(1)  #Fix this

    more_button = WebDriverWait(browser, WAIT_TIME).until(
        EC.element_to_be_clickable((By.ID, 'action-panel-overflow-button'))
    )
    actions = ActionChains(browser)
    actions.move_to_element(more_button)
    WebDriverWait(browser, WAIT_TIME).until(
        EC.element_to_be_clickable((By.ID, 'action-panel-overflow-button'))
    )
    actions.click(more_button)
    actions.perform()

    transcript_button = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="action-panel-overflow-menu"]/li[2]/button'))
    )
    actions = ActionChains(browser)
    actions.move_to_element(transcript_button)
    WebDriverWait(browser, WAIT_TIME).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="action-panel-overflow-menu"]/li[2]/button'))
    )
    actions.click(transcript_button)
    actions.perform()

    english_button = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="watch-transcript-container"]/div[2]/div[1]/button'))
    )
    actions = ActionChains(browser)
    actions.move_to_element(english_button)
    WebDriverWait(browser, WAIT_TIME).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="watch-transcript-container"]/div[2]/div[1]/button'))
    )
    actions.click(english_button)
    actions.perform()

    language_button = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located((By.XPATH, '//button[@class="yt-ui-menu-item yt-uix-menu-close-on-select yt-uix-button-menu-item" and ./span[contains(., "English")]]'))
    )
    actions = ActionChains(browser)
    actions.move_to_element(language_button)
    WebDriverWait(browser, WAIT_TIME).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="yt-ui-menu-item yt-uix-menu-close-on-select yt-uix-button-menu-item" and ./span[contains(., "English")]]'))
    )
    actions.click(language_button)
    actions.perform()

if __name__ == '__main__':
    url = input("Enter url of page: ")

    target_string = input("Enter the word you're searching for: ")

    browser = webdriver.Chrome('/Users/chromedriver')
    try:
        browser.get(url)
    except:
        print("Fatal error: Invalid URL")
        sys.exit(0)

    WebDriverWait(browser, WAIT_TIME).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="watch-transcript-container"]/div[2]/div[1]/button/span'), 'English')
    )
    WebDriverWait(browser, WAIT_TIME).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'caption-line-text'))
    )

    soup = BeautifulSoup(browser.page_source, 'lxml')
    soup.prettify()
    caption_time_dictionary = extract_transcript(soup)
    times = get_caption_times(caption_time_dictionary, target_string)
    if(times):
        seconds = (times[0])[-2:]
        minutes = (times[0])[:-3]
        new_url = url + '&t={:s}m{:s}s'.format(minutes, seconds)
        print(new_url)
        browser.get(new_url)
