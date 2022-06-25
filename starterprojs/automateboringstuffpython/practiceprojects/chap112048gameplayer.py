from random import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random


def playgame():
    driver = webdriver.Firefox()
    driver.get('https://play2048.co')

    key_select = [Keys.UP, Keys.DOWN,Keys.LEFT,Keys.RIGHT]

    gamestatsElem = driver.find_element_by_css_selector('.game-container p')
    htmlElem = driver.find_element_by_css_selector('html')

    while gamestatsElem.text != 'Game over!':
        htmlElem.send_keys(key_select[random.randint(0,3)])
        print('sending = ', random.randint(0,3))
        gamestatsElem = driver.find_element_by_css_selector('.game-container p')
    
    score = driver.find_element_by_css_selector('.score-container').text
    print('score is ', score, '\nclose now')
    driver.close()
    exit()



if __name__ == '__main__':
    playgame()