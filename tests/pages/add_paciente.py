import conftest
from selenium.webdriver.common.by import By
from time import sleep

class Paciente_Add:

    def __init__(self):
        self.driver = conftest.driver

    def adicionar_paciente(self, nome, idade, email, telefone):
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button').click()
        sleep(2)
        
        campo_paciente = self.driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/div/div[2]/input')
        campo_paciente.send_keys(nome)
        
        campo_idade = self.driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[2]')
        campo_idade.send_keys(idade)

        campo_email = self.driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[3]')
        campo_email.send_keys(email)

        campo_telefone = self.driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[4]')
        campo_telefone.send_keys(telefone)

        sleep(2)

        # clicar em salvar
        self.driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[5]').click()
