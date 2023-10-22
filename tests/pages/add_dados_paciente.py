from time import sleep
from selenium.webdriver.common.by import By
import conftest

class Add_Dados_Paciente:

    def __init__(self):
        self.driver = conftest.driver

    def adicionar_dados(self):
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/a[2]/div').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/a/div/p[1]').click()
        self.driver.find_element(By.CLASS_NAME, 'btn-outline-success').click()
        sleep(2)
        # dados de teste
        self.driver.find_element(By.NAME, 'peso').send_keys('78')
        self.driver.find_element(By.NAME, 'altura').send_keys('165')
        self.driver.find_element(By.NAME, 'gordura').send_keys('40')
        self.driver.find_element(By.NAME, 'musculo').send_keys('60')
        self.driver.find_element(By.NAME, 'hdl').send_keys('12')
        self.driver.find_element(By.NAME, 'ldl').send_keys('12')
        self.driver.find_element(By.NAME, 'ctotal').send_keys('60')
        self.driver.find_element(By.NAME, 'triglicerídios').send_keys('23')
        sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'btn-success').click()
        sleep(1)
