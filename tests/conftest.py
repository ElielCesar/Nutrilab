import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# define a variavel de forma global e acessivel entre arquivos
driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():
    # setup
    global driver
    '''todo esse bloco será sempre executado antes do teste iniciar,
    dos testes que estiverem usando o decorator com esse nome de 
    funcão é claro.
    '''
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/auth/login/')
    driver.maximize_window()
    driver.find_element(By.NAME, 'usuario').send_keys('eliel')
    driver.find_element(By.NAME, 'senha').send_keys('Eliel123')
    driver.find_element(By.CLASS_NAME, 'btn-first').click()

    # onde os testes executam
    yield 

    # teardown
    sleep(3)
    driver.close()

@pytest.fixture()
def setup_teardown_login():
    # setup
    global driver
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/auth/login/')
    driver.maximize_window()
    
    yield

    # teardown
    sleep(3)
    driver.close()