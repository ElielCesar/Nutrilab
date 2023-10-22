import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.add_dados_paciente import Add_Dados_Paciente

@pytest.mark.usefixtures('setup_teardown')
class Test_Add_Dados_Pacientes:

    def test_add_dados_paciente(self):
        driver = conftest.driver
        form = Add_Dados_Paciente()
        form.adicionar_dados()
        msg_sucesso = driver.find_element(By.CLASS_NAME, 'alert-success')
        assert msg_sucesso.is_displayed()
        assert msg_sucesso.text == 'Dados cadastrado com sucesso'

