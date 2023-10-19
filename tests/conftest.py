import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/auth/login/')
    driver.maximize_window()

    # onde os testes executam
    yield 

    # teardown
    driver.close()
