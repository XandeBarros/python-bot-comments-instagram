from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path='C:\geckodriver\geckodriver.exe')

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
        #//button[@class='sqdOP  L3NKy   y3zKF     ']
        #//input[@name='username']
        #//input[@name='password']
        label_user = driver.find_element_by_name("username")
        label_user.click()
        label_user.clear()
        label_user.send_keys(self.username)
        label_password = driver.find_element_by_name("password")
        label_password.click()
        label_password.clear()
        label_password.send_keys(self.password)
        button_login = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
        button_login.click()
        time.sleep(5)
        '''driver.get("https://www.instagram.com/p/CJi60PIAymX/")'''
        self.comment_giveaway('CJt_Cn0Axll')

    @staticmethod
    def write_as_a_person(comment, where_comment):
        for letra in comment:
            where_comment.send_keys(letra)
            time.sleep(random.randint(1, 5)/30)

    def comment_giveaway(self, link):
        driver = self.driver
        driver.get("https://www.instagram.com/p/" + link + "/")
        time.sleep(5)
        try:
            comments = [ # insira aqui seus arrobas a serem marcados ;)
                ]

            auxiliary_number = 0
            comments_len = len(comments)

            comment_field = driver.find_element_by_xpath("//textarea[@class='Ypffh']")
            comment_field.click()
            comment_field = driver.find_element_by_xpath("//textarea[@class='Ypffh focus-visible']")
            time.sleep(random.randint(2, 5))
            print("It will be " + str(comments_len) + " comments")
            while auxiliary_number <= comments_len:
                self.write_as_a_person(comments[auxiliary_number], comment_field)
                time.sleep(random.randint(30,60))
                #driver.find_element_by_class_name("sqdOP yWX7d    y3zKF     ").click()
                comment_field.send_keys(Keys.ENTER)
                time.sleep(7)
                print(comments[auxiliary_number] + "has already been commented")
                auxiliary_number += 1
        except Exception as e:
            print(e)
            time.sleep(5)
xandebot = InstagramBot('Alexanblau_', 'Alexandre20+')
xandebot.login()

