import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lxml import html
from bs4 import BeautifulSoup
import time

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

    more_button = WebDriverWait(browser, 6).until(
        EC.presence_of_element_located((By.ID, 'action-panel-overflow-button'))
    )
    actions = ActionChains(browser)
    actions.move_to_element(more_button)
    WebDriverWait(browser, 6).until(
        EC.element_to_be_clickable((By.ID, 'action-panel-overflow-button'))
    )
    actions.click(more_button)
    actions.perform()

    transcript_button = WebDriverWait(browser, 6).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="action-panel-overflow-menu"]/li[2]/button'))
    )
    actions = ActionChains(browser)
    actions.move_to_element(transcript_button)
    WebDriverWait(browser, 6).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="action-panel-overflow-menu"]/li[2]/button'))
    )
    actions.click(transcript_button)
    actions.perform()

    english_button = WebDriverWait(browser, 6).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="watch-transcript-container"]/div[2]/div[1]/button'))
    )
    actions = ActionChains(browser)
    actions.move_to_element(english_button)
    WebDriverWait(browser, 6).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="watch-transcript-container"]/div[2]/div[1]/button'))
    )
    actions.click(english_button)
    actions.perform()

    english_button2 = WebDriverWait(browser, 6).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="aria-menu-id-7"]/button'))
    )
    actions = ActionChains(browser)
    actions.move_to_element(english_button2)
    WebDriverWait(browser, 6).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="aria-menu-id-7"]/button'))
    )
    actions.click(english_button2)
    actions.perform()

    WebDriverWait(browser, 6).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'caption-line-text'))
    )

    soup = BeautifulSoup(browser.page_source, 'lxml')
    soup.prettify()
    caption_time_dictionary = extract_transcript(soup)
    times = get_caption_times(caption_time_dictionary, word)
    print(times)
