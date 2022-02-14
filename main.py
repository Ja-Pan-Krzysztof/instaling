from dotenv import load_dotenv
from os import getenv

from instalingLogIn import InstalingLogIn

load_dotenv()

if __name__ == '__main__':
    i = InstalingLogIn(
        username=getenv('_USERNAME'),
        password=getenv('_PASSWORD')
    )
