import pytest
import requests

class TestLogin:
    
    def test_successful_login(self):
        # Пример с API тестированием
        response = requests.post(
            "https://api.example.com/login",
            json={"username": "test", "password": "test"}
        )
        assert response.status_code == 200
        assert "token" in response.json()
    
    def test_invalid_credentials(self):
        response = requests.post(
            "https://api.example.com/login",
            json={"username": "wrong", "password": "wrong"}
        )
        assert response.status_code == 401
    
    @pytest.mark.ui
    def test_login_ui(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        try:
            driver.get("https://example.com/login")
            driver.find_element(By.ID, "username").send_keys("test")
            driver.find_element(By.ID, "password").send_keys("test")
            driver.find_element(By.ID, "submit").click()
  
            assert "Dashboard" in driver.title
        finally:
            driver.quit()
