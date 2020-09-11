from selenium import webdriver
from time import sleep
from random import choice, randrange


class Instagram:
    def __init__(self, driver, url_instagram_post):

        self.__driver = driver
        self.__url_instagram = 'https://www.instagram.com/'
        self.__url_intagram_post = url_instagram_post

        # Elements of the intagram login page #xPath
        self.__input_user_name = 'username'  # name
        self.__input_user_password = 'password'  # name
        # xPath
        self.__btn_login = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button'

        # Elements of the intagram post page #xPath

        self.__input_comment = 'Ypffh'  # class
        self.__btn_post_comment = '#react-root > section > main > div > div.ltEKP > article > div > div.eo2As > section.sH9wk._JgwE > div > form > button'

    def navigate(self):
        self.__driver.get(self.__url_instagram)
        sleep(2)

    def login(self, user_name, password):
        
        print("Login Intagram")
        self.__driver.find_element_by_name(
            self.__input_user_name).send_keys(user_name)
        self.__driver.find_element_by_name(
            self.__input_user_password).send_keys(password)
        self.__driver.find_element_by_xpath(self.__btn_login).click()
        sleep(2)
        self.__driver.get(self.__url_intagram_post)
        sleep(4)

    def __choice_users_name_post(self, comments_list, user_number_per_comment):
        comments_list = comments_list
        comments = []
        while len(comments) < user_number_per_comment:
            commnet = choice(comments_list)
            comments.append(f'@{commnet}'.strip())
            comments_list.remove(commnet)
        return comments

    def comment(self, comments_list, user_number_per_comment, comment_number=1):
        print("Comment")
        comments_list_copy = comments_list [:]

        for i in range(comment_number):

            if len(comments_list_copy) == 0:
                comments_list_copy = comments_list[:]
            index = 0
            choiceusers_name_post = self.__choice_users_name_post(
                comments_list_copy, user_number_per_comment)
            self.__driver.find_element_by_class_name(
                self.__input_comment).click()
            for element in choiceusers_name_post:

                self.__driver.find_element_by_class_name(
                    self.__input_comment).send_keys(f'{element} ')
            sleep(2)
            self.__driver.find_element_by_css_selector(
                self.__btn_post_comment).click()
            print(f'Comentario de numero {i+1} => {choiceusers_name_post}')
            sleep(8)
            self.__driver.refresh()
            sleep(60+randrange(0, 9))
