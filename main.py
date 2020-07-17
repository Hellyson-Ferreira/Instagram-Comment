from instagram import Instagram
from selenium import webdriver
from time import sleep


URL = "https://www.instagram.com/p/CCpHERaFpm6/"
USERNAME = "XXXXXXXXXXXX"
PASSWORD = "xxxxxxxxxxxxxxxxx"
COMMENT_NUMBER = 1000

COMMENT_LIST = [
    '@felipeanders.on__',
    '@ciellen_santos',
    '@francinete.franca.16',
    '@francianesantos1607',
    '@magda_36.1',
    '@ytaciria',
    '@antoniaantoniabrandao',

]
USER_NUMBER_PER_COMMENT = 2

DRIVER = webdriver.Chrome()

instagram = Instagram(DRIVER, URL)
instagram.navigate()
instagram.login(USERNAME, PASSWORD)
instagram.comment(COMMENT_LIST, USER_NUMBER_PER_COMMENT, COMMENT_NUMBER)
