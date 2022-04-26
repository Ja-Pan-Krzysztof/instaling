#!E:\Python\..Python_venv\instaling\Scripts\python
from dotenv import load_dotenv
from os import getenv

from instalingLogIn import InstalingLogIn
# from InstalingSolving import InstalingSolving

load_dotenv()

if __name__ == '__main__':
    InstalingLogIn(
        username=getenv('_USERNAME'),
        password=getenv('_PASSWORD')
    )
