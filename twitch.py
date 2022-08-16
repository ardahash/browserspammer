from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from selenium.webdriver.common.keys import Keys

spamlink = "put any link here, should be a url or like twitch.tv/botter or youtube.com/videolink"
driver.get("https://www.croxyproxy.net")
driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(spamlink)
driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(Keys.ENTER)
