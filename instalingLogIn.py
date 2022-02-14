from selenium import webdriver
from selenium.webdriver.common.by import By

from words import words

from time import sleep


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

    def _parameters(self):
        print('Loading... _parameters()')
        self.driver.implicitly_wait(5)
        self.username_input = self.driver.find_element(By.ID, 'log_email')
        self.password_input = self.driver.find_element(By.ID, 'log_password')
        self.button_log_in = self.driver.find_element(By.XPATH, '//button[@type="submit"]')

    def _account_log_in(self):
        print('Loading... InstalingLogIn / account_log_in')

        current_url = self.driver.current_url

        self.username_input.send_keys(self.username)
        self.password_input.send_keys(self.password)

        self.button_log_in.click()
        sleep(1)

        if self.driver.current_url != current_url:
            self._panel_student()

        else:
            print('Błędny login lub hasło')
            self.driver.close()
            self.driver.quit()

    def _panel_student(self):
        current_url = self.driver.current_url

        self.student_panel = self.driver.find_element(By.ID, 'student_panel')
        self.start_button = self.student_panel.find_element(By.XPATH, '//a[@style="width: 200px;"]')

        self.start_button.click()

        if self.driver.current_url != current_url:
            try:
                self.driver.find_element(By.ID, 'start_session_button').click()
                sleep(2)
                self._solving_words()

            except:
                self.driver.find_element(By.ID, 'continue_session_button').click()
                sleep(2)
                self._solving_words()

        else:
            sleep(2)
            self.driver.quit()

    def _solving_words(self):
        print('_solving_words')
        num_words = 1

        self.translation_input = self.driver.find_element(By.ID, 'answer')
        self.send_answer = self.driver.find_element(By.ID, 'check')
        self.next_word = self.driver.find_element(By.ID, 'next_word')

        try:
            while True:
                translete_words = self.driver.find_element(By.CLASS_NAME, 'translations')
                word = words.get(translete_words.text)

                self.translation_input.send_keys(word)
                sleep(4)

                self.send_answer.click()
                print(f'To było {num_words} słówko.')
                sleep(4)

                self.next_word.click()
                sleep(1.5)

                num_words += 1

        except:
            try:
                self.driver.find_element(By.ID, 'return_mainpage').click()

            except:
                sleep(200)
                print('Coś nie poszło')

            finally:
                sleep(2)
                self.driver.quit()
