from selenium.webdriver.common.by import By 
from django.test import LiveServerTestCase
import pytest
from time import sleep
import conftest

@pytest.mark.usefixtures("setup_teardown_login")
class Test_Login_Page(LiveServerTestCase):

    # Testa a presença da imagem no elemento
    def test_1_logo_projeto_existe(self):
        driver = conftest.driver 
        imagem = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/h2/img')
        sleep(3)
        assert imagem.is_displayed()

    # Testa login bem sucedido
    def test_2_login_sucesso(self):
        driver = conftest.driver
        driver.find_element(By.NAME, 'usuario').send_keys('eliel')
        driver.find_element(By.NAME, 'senha').send_keys('Eliel123')
        driver.find_element(By.CLASS_NAME, 'btn-first').click()
        sleep(2)
        titulo_navbar = driver.find_element(By.CLASS_NAME, 'navbar-brand')
        assert titulo_navbar.is_displayed()

    # testa mensagem de falha de login
    def test_3_login_falha(self):
        driver = conftest.driver
        driver.find_element(By.NAME, 'usuario').send_keys('eliel')
        driver.find_element(By.NAME, 'senha').send_keys('Eliel123errada')
        driver.find_element(By.CLASS_NAME, 'btn-first').click()
        sleep(2)
        msg_falha = driver.find_element(By.CLASS_NAME, 'alert-danger')
        assert msg_falha.is_displayed()
        assert msg_falha.text == 'Usuário ou Senha inválidos'


@pytest.mark.usefixtures("setup_teardown")
class Test_Cadastrar_Paciente(LiveServerTestCase):
    
    # cadastrar novo paciente
    def test_1_novo_paciente(self):
        driver = conftest.driver
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button').click()
        sleep(3)
        
        paciente = driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/div/div[2]/input')
        paciente.send_keys('selenium')
        
        idade = driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[2]')
        idade.send_keys('33')

        email = driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[3]')
        email.send_keys('selenium@gmail.com')

        telefone = driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[4]')
        telefone.send_keys('069 99246-5207')
        sleep(2)

        # clicar em salvar
        driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[5]').click()
    
        msg_sucesso = driver.find_element(By.CLASS_NAME, 'alert-success')
        assert msg_sucesso.is_displayed()

        # testar mensagem de falha de usuário duplicado

    # cadastrar novo paciente
    def test_2_paciente_repetido_erro(self):
        driver = conftest.driver
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button').click()
        sleep(3)
        
        paciente = driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/div/div[2]/input')
        paciente.send_keys('selenium')
        
        idade = driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[2]')
        idade.send_keys('33')

        email = driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[3]')
        email.send_keys('selenium@gmail.com')

        telefone = driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[4]')
        telefone.send_keys('069 99246-5207')
        sleep(2)

        # clicar em salvar
        driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/form/input[5]').click()
    
        msg_erro = driver.find_element(By.CLASS_NAME, 'alert-danger')
        assert msg_erro.is_displayed()
