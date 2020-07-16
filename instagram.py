from selenium import webdriver
from time import sleep
from random import choice


class Instagram:
    def __init__(self, driver, urlIntagramPost):

        self.__driver = driver
        self.__urlIntagram = 'https://www.instagram.com/'
        self.__urlIntagramPost = urlIntagramPost

        # Elements of the intagram login page #xPath
        self.__InputUserName = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/Input/input'
        self.__InputPassword = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'
        self.__BtnLogin = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button'

        # Elements of the intagram post page #xPath

        self.__inputComment = '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/textarea'
        self.__btnPostComment = '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/button'

    def navigate(self):
        self.driver.get(self.urlIntagram)
        sleep(2)

    def login(self, userName, password):
        self.driver.find_element_xpath(
            self.__InputUserName).send_keys(userName)
        self.driver.find_element_xpath(
            self.__InputPassword).send_keys(password)
        self.driver.find_element_xpath(self.__BtnLogin).click()
        sleep(2)

    def userNamePost(self, commentsList, indexList, commentNumberPerComment=1):

        if userNumberPerComment == 1:
            return indexList
        else:
            listIndex = [index]
            for elementIndex in range(commentNumberPerComment):
                if indexList > (len(commentList) - 1):  
                    indexList = 0

                listIndex.append(index + 1)

    def comment(self, commentsList, commentNumberPerComment=1, commentNumber=1):
        indexList = 0
        for i in range(numberComment):
            
            self.driver.find_element_xpath(self.__inputComment).send_keys()
            self.driver.find_element_xpath(self.__btnPostComment).click()
            
