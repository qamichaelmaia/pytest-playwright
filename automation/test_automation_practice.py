from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.faker_generator import generate_user_data

import time

def test_automation_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Gera os dados com Faker
        user_data = generate_user_data()

        # Login Page
        login_page = LoginPage(page)
        login_page.navigate_to("https://automationexercise.com/login")
        login_page.fill_name_and_email(user_data["name"], user_data["email"])
        login_page.click_signup()
        time.sleep(3)

        # Signup Page
        signup_page = SignupPage(page)
        signup_page.fill_signup_form(user_data)
        signup_page.submit_form()

        # Verificação
        confirmation_message = page.locator('//*[@id="form"]/div/div/div/h2/b').text_content()
        assert confirmation_message == "Account Created!", f"Erro: '{confirmation_message}' não corresponde ao esperado."

        time.sleep(8)

        browser.close()
