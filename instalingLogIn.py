from selenium import webdriver
from selenium.webdriver.common.by import By

from words import words

from time import sleep
from random import randrange, random
import logging.config

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=True)
logger = logging.getLogger(__name__)


class InstalingLogIn:
    _PATH = 'E:/Python/..Python_venv/chromedriver.exe'
    _DRIVER = webdriver.Chrome(_PATH)
    _DRIVER.get('https://instaling.pl/teacher.php?page=login')

    def __init__(self, username, password):
        self.driver = self._DRIVER
        self.username = username
        self.password = password

        self._parameters()
        self._account_log_in()

        self.new_word_list = []

    @staticmethod
    def num():
        while True:
            a = 4 * random()
            if a > 1.2:
                continue

            else:
                return a

    def _parameters(self):
        logger.info('Loading... [ _parameters() ]')
        self.driver.implicitly_wait(5)
        self.username_input = self.driver.find_element(By.ID, 'log_email')
        self.password_input = self.driver.find_element(By.ID, 'log_password')
        self.button_log_in = self.driver.find_element(By.XPATH, '//button[@type="submit"]')

    def _account_log_in(self):
        logger.info('Loading... [ _account_log_in() ]')

        current_url = self.driver.current_url

        self.username_input.send_keys(self.username)
        self.password_input.send_keys(self.password)

        self.button_log_in.click()
        sleep(self.num())

        if self.driver.current_url != current_url:
            self._panel_student()

        else:
            logger.error('Bad login or password')
            self.driver.close()
            self.driver.quit()

    def _panel_student(self):
        logger.info('Loading... [ _panel_student() ]')
        current_url = self.driver.current_url

        self.student_panel = self.driver.find_element(By.ID, 'student_panel')
        self.start_button = self.student_panel.find_element(By.XPATH, '//a[@style="width: 200px;"]')

        self.start_button.click()

        if self.driver.current_url != current_url:
            try:
                self.driver.find_element(By.ID, 'start_session_button').click()
                self._solving_words()

            except:
                self.driver.find_element(By.ID, 'continue_session_button').click()
                self._solving_words()

        else:
            sleep(randrange(1, 5))
            self.driver.quit()

    def _solving_words(self):
        logger.info('Loading... [ _solving_words() ]')
        num_words = 1

        self.translation_input = self.driver.find_element(By.ID, 'answer')
        self.send_answer = self.driver.find_element(By.ID, 'check')
        self.next_word = self.driver.find_element(By.ID, 'next_word')

        try:
            while True:
                logger.info('Loop [ Try | While True ]')

                '''if word is None:
                    new_word = str(input('Podaj odpowiedź : '))
                    self.new_word_list.append(f'{translete_words}: {new_word}')

                    word = new_word'''

                try:
                    logger.info('Loop [ Try | While True | Try ]')
                    self.driver.find_element(By.ID, 'dont_know_new').click()

                    sleep(self.num())

                    self.driver.find_element(By.ID, 'skip').click()

                except:
                    logger.info('Loop [ Try | While True | Except ]')

                    sleep(self.num())
                    translete_words = self.driver.find_element(By.CLASS_NAME, 'translations')
                    word = words.get(translete_words.text)

                    sleep(randrange(1, 4))
                    self.translation_input.send_keys(word)

                    sleep(random())

                    self.send_answer.click()
                    print(f'To było {num_words} słówko.')
                    sleep(self.num())

                    self.next_word.click()
                    sleep(self.num())

                num_words += 1

        except:
            logger.info('not Loop [ Except ]')
            try:
                logger.info('not Loop [ Except | Try ]')
                self.driver.find_element(By.ID, 'return_mainpage').click()

            except:
                logger.info('not Loop [ Except | Except ]')
                sleep(self.num())

            finally:
                logger.info('not Loop [ Except | Finally ]')
                sleep(self.num())
                print('\n\tGratulacje ! Dzisiejsza sesja wykonana !\n')

                self.driver.quit()
