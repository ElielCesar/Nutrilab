from selenium.webdriver.common.by import By 
from django.test import LiveServerTestCase
from time import sleep
import pytest
import conftest

# aqui vão vir os page objects para otimizar o código
from pages.login import Login_Page

@pytest.mark.usefixtures("setup_teardown_login")
class Test_Login_Page(LiveServerTestCase):

    # Testa a presença da imagem no elemento
    def test_1_logo_projeto_existe(self):
        driver = conftest.driver 
        imagem = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/h2/img')
        assert imagem.is_displayed()


    # Testa login bem sucedido
    def test_2_login_valido(self):
        driver = conftest.driver
        login = Login_Page()
        login.fazer_login('eliel', 'Eliel123')
        titulo_navbar = driver.find_element(By.CLASS_NAME, 'navbar-brand')
        assert titulo_navbar.is_displayed()


    # testa mensagem de falha de login
    def test_3_login_invalido(self):
        driver = conftest.driver
        login = Login_Page()
        login.fazer_login('eliel', 'Elielerrada')
        msg_falha = driver.find_element(By.CLASS_NAME, 'alert-danger')
        assert msg_falha.is_displayed()
        assert msg_falha.text == 'Usuário ou Senha inválidos'
        