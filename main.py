from instagram import Instagram
from selenium import webdriver
from time import sleep

#886
URL_POST = "https://www.instagram.com/p/CDML-F1h_ib/"
USERNAME = "XXXXXXX"
PASSWORD = "XXXXXXXXXXX"
COMMENT_NUMBER = 1000
COMMENT_LIST = [
    '@adriel.victrre',
    '@felipeanders.on__',
    '@franferreira1023',
    '@joao.vvi',
    '@__hellysonferreira__',
    '@ray_santtory',
    '@livia_magalhaesbkl',
    '@ayslanguima',
    '@basilioelcio',
    '@felipeanderson__',
    '@luaneisabele82',
    '@joseemanuelsame',
    '@joseemanuel778',
]

USER_NUMBER_PER_COMMENT = 1

DRIVER = webdriver.Chrome()

instagram = Instagram(DRIVER,URL_POST)
instagram.navigate()
instagram.login(USERNAME, PASSWORD)
instagram.comment(COMMENT_LIST, USER_NUMBER_PER_COMMENT, COMMENT_NUMBER)
