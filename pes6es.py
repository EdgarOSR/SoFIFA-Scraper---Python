from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from subprocess import CREATE_NO_WINDOW    
    
class pes6es:
    def __init__(self):
        self.url = 'https://www.pes6.es/stats/fifa-to-pes6.php'

    def __drive_initialize(self):
        chrome_service = ChromeService(ChromeDriverManager().install())
        chrome_service.creationflags = CREATE_NO_WINDOW
        chrome_options = Options()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def __drive_close(self):
        self.driver.quit()

    def convert_offline(self, json):
        self.__drive_initialize()
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, '#showManualStats').click()
        self.driver.find_element(By.CSS_SELECTOR, '#offlineStats').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#offlineStats').send_keys(str(json))
        self.driver.find_element(By.CSS_SELECTOR, '#convertOffline').click()
        response = ''
        while response == '':
            response = self.driver.find_element(By.CSS_SELECTOR, '#statsToCopy').text.strip()
        response = response.replace('★','*')
        self.__drive_close()
        return response

    def convert_player(self, player):
        self.__drive_initialize()
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, '#freeSoFifa').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#freeSoFifa').send_keys(str(player))
        self.driver.find_element(By.CSS_SELECTOR, '#convertFreeSoFifa').click()
        response = ''
        while response == '':
            response = self.driver.find_element(By.CSS_SELECTOR, '#statsToCopy').text.strip()
        response = response = response.replace('★','*')
        self.__drive_close()
        return response