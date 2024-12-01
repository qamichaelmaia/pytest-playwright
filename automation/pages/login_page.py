from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = 'xpath=//*[@id="form"]/div/div/div[3]/div/form/input[2]'
        self.email_input = 'xpath=//*[@id="form"]/div/div/div[3]/div/form/input[3]'
        self.signup_button = 'xpath=//*[@id="form"]/div/div/div[3]/div/form/button'

    def navigate_to(self, url: str):
        self.page.goto(url)

    def fill_name_and_email(self, name: str, email: str):
        self.page.fill(self.name_input, name)
        self.page.fill(self.email_input, email)

    def click_signup(self):
        self.page.click(self.signup_button)
