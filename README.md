# INSTALING BOT 🐍
***

##### This bot solving your daily session on [Instaling](https://instaling.pl/). It's your end of tiring typing words. It's time for Instaling Bot!

&nbsp;

### INSTALATION
***

 - [Python 3.10.2](https://www.python.org/downloads/release/python-3102/)
   - Install Selenium
      ```bash
          pip install selenium  # I used 4.1.0
      ```
   - Install python-dotenv
      ```bash
          pip install python-dotenv  # I used 0.19.2
      ```
   - Or you can install everything:
     ```python
        pip install -r requirements.txt
     ```
 - Download one of the selected webdrivers:
   * [Chrome](https://chromedriver.chromium.org/)
   * [Firefox](https://github.com/mozilla/geckodriver/releases)
   * [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
  
&nbsp;

### PREPARATION
***

* Download this repository:
  * If you use GIT :
     ```git
         git clone https://github.com/Ja-Pan-Krzysztof/instaling.git
     ```
* Create file `.env` and enter that data :
   ```dotenv
        _USERNAME=<your_login>
        _PASSWORD=<your_password>
   ```
* If are you using your own venv, delete the first line in `main.py`
   ```python
        #!E:\Python\..Python_venv\instaling\Scripts\python
   ```
  to your file path.  
   Else delete this line if are you using default interpreter.

&nbsp;

* Change the path in `instalingLogIn` to yours:
  * Firefox :
     ```python
          _PATH = r'<your path to webdriver>'
          _DRIVER = webdriver.Firefox(executable_path=_PATH)
    ```
  * Chrome :
     ```python
          _PATH = r'<your path to webdriver>'  # Line 15
          _DRIVER = webdriver.Chrome(executable_path=_PATH)  # Line 16
    ```
  * Safari : 
         I don't have this ~~supercomputer~~ ( This isn't computer, this is a MacBook )
&nbsp;
   
### USE
***

* Windows :
   ```bash
      py main.py
   ```
* Linux / MacOS :
   ```bash
      python3 main.py
   ```
  
&nbsp;
  
### Thanks for use this 🐍
