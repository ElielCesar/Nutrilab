'''
Usando o padrão Page object é possivel modularizar determinadas acoes 
e reaproveitas esses módulos / classes em diversos outros testes, 
se o processo de login mudar, só preciso mexer aqui.
'''

import conftest
from selenium.webdriver.common.by import By

class Login_Page:
    
    def __init__(self):
        self.driver = conftest.driver

    def fazer_login(self, usuario, senha):
        self.driver.find_element(By.NAME, 'usuario').send_keys(usuario)
        self.driver.find_element(By.NAME, 'senha').send_keys(senha)
        self.driver.find_element(By.CLASS_NAME, 'btn-first').click()

