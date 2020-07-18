from selenium import webdriver
from time import sleep
from random import choice,randrange


class Instagram:
    def __init__(self, driver, urlIntagramPost):

        self.__driver = driver
        self.__urlIntagram = 'https://www.instagram.com/'
        self.__urlIntagramPost = urlIntagramPost

        # Elements of the intagram login page #xPath
        self.__InputUserName = 'username'  # name
        self.__InputPassword = 'password'  # name
        # xPath
        self.__BtnLogin = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button'

        # Elements of the intagram post page #xPath

        self.__inputComment = 'Ypffh'  # class
        self.__btnPostComment = '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/button'

    def navigate(self):
        self.__driver.get(self.__urlIntagram)
        sleep(2)

    def login(self, userName, password):
        print("Login Intagram")
        self.__driver.find_element_by_name(
            self.__InputUserName).send_keys(userName)
        self.__driver.find_element_by_name(
            self.__InputPassword).send_keys(password)
        self.__driver.find_element_by_xpath(self.__BtnLogin).click()
        sleep(2)
        self.__driver.get(self.__urlIntagramPost)
        sleep(4)

    def __choiceusersNamePost(self, commentsList, userNumberPerComment):
        commentsList = commentsList[:]
        comments = []
        while len(comments) < userNumberPerComment:
            commnet = choice(commentsList)
            comments.append(commnet)
            commentsList.remove(commnet)
        return comments

    def comment(self, commentsList, userNumberPerComment, commentNumber=1):
        print("Comment")
        for i in range(commentNumber):
            index = 0
            choiceusersNamePost = self.__choiceusersNamePost(
                commentsList, userNumberPerComment)
            self.__driver.find_element_by_class_name(
                    self.__inputComment).click()
            for element in choiceusersNamePost:

                self.__driver.find_element_by_class_name(
                    self.__inputComment).send_keys(f'{element} ')
            sleep(2)
            self.__driver.find_element_by_xpath(self.__btnPostComment).click()
            print(f'Comentario de numero {i+1} => {choiceusersNamePost}')
            sleep(8)
            self.__driver.refresh()
            sleep(60+randrange(0, 9))
