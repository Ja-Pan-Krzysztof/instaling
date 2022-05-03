#!E:\Python\..Python_venv\instaling\Scripts\python
from dotenv import load_dotenv
from os import getenv
from platform import release

from instalingLogIn import InstalingLogIn
# from InstalingSolving import InstalingSolving

load_dotenv()

if __name__ == '__main__':
    if release() == '11':
        print('Please change windows system to version 10 :)')

    else:
        InstalingLogIn(
            username=getenv('_USERNAME'),
            password=getenv('_PASSWORD')
        )