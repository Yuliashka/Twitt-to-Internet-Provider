# INTERNET SPEED WEBSITE: https://www.speedtest.net/


# IMPORTING SELENIUM PACKAGE:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# INTERNET PROVIDER CONTRACT INFO:
PROMISED_DOWN = 100
PROMISED_UP = 20

# PATH TO CHROM DRIVER:
chrom_driver_path = "C:\Development\chromedriver.exe"

# TWITTER ACCOUNT LOGIN INFO:
TWITTER_ACCOUNT = "your account name"
TWITTER_PASSWORD = "your password"

# CREATING A CLASS:
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrom_driver_path)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP


    def get_internet_speed(self):
        # GETTING THE INTERNET TEST PAGE:
        self.driver.get("https://www.speedtest.net/")
        consent_button = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        time.sleep(5)
        consent_button.click()
        time.sleep(5)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        time.sleep(5)
        go_button.click()
        time.sleep(40)
        down_info = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        time.sleep(2)
        self.down = down_info.text
        print(f"The real download speed: {self.down}")
        up_info = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        time.sleep(2)
        self.up = up_info.text
        print(f"The real upload speed: {self.up}")
        time.sleep(5)



    def tweet_at_provider(self):
        time.sleep(2)
        self.driver.get("https://twitter.com/twitter")
        time.sleep(2)
        enter_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div[1]/a/div/span/span')
        time.sleep(2)
        enter_button.click()
        time.sleep(2)
        login_name = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        time.sleep(2)
        login_name.send_keys(TWITTER_ACCOUNT)
        time.sleep(2)
        login_password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        time.sleep(2)
        login_password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        time.sleep(2)
        login_button.click()
        time.sleep(5)
        home_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]/div')
        time.sleep(2)
        home_button.click()
        time.sleep(2)
        message_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        time.sleep(2)
        message_input.send_keys(f'Hey! Internet Provider (YOU CAN PUT HERE its name), why is my internet speed {my_bot.down}down/ {my_bot.up}up when I pay for {PROMISED_DOWN}down/ {PROMISED_UP}up!?')
        time.sleep(5)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        time.sleep(5)
        tweet_button.click()



# CREATING A CLASS OBJECT:
my_bot = InternetSpeedTwitterBot()

# CALLING CLASS METHODS:
my_bot.get_internet_speed()
my_bot.tweet_at_provider()


