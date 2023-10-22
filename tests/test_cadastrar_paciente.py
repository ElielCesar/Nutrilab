from selenium.webdriver.common.by import By 
from django.test import LiveServerTestCase
import pytest
import conftest

# aqui vão vir os page objects para otimizar o código
from pages.cadastrar_paciente import Paciente_Add

@pytest.mark.usefixtures("setup_teardown")
class Test_Cadastrar_Paciente(LiveServerTestCase):
    
    # cadastrar novo paciente
    def test_1_novo_paciente(self):
        driver = conftest.driver
        paciente = Paciente_Add()
        paciente.adicionar_paciente('selenium', '33', 'selenium@gmail.com', '069 2121-2323')
        msg_sucesso = driver.find_element(By.CLASS_NAME, 'alert-success')
        assert msg_sucesso.is_displayed()


    # cadastrar paciente repetido
    def test_2_paciente_repetido(self):
        driver = conftest.driver
        paciente = Paciente_Add()
        paciente.adicionar_paciente('selenium', '33', 'selenium@gmail.com', '069 2121-2323')
        msg_erro = driver.find_element(By.CLASS_NAME, 'alert-danger')
        assert msg_erro.is_displayed()
