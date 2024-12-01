from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.gender_checkbox = 'xpath=//*[@id="id_gender1"]'
        self.password_input = 'xpath=//*[@id="password"]'
        self.first_name_input = 'xpath=//*[@id="first_name"]'
        self.last_name_input = 'xpath=//*[@id="last_name"]'
        self.company_input = 'xpath=//*[@id="company"]'
        self.address_input = 'xpath=//*[@id="address1"]'
        self.country_dropdown = '//*[@id="country"]'
        self.state_input = 'xpath=//*[@id="state"]'
        self.city_input = 'xpath=//*[@id="city"]'
        self.zipcode_input = 'xpath=//*[@id="zipcode"]'
        self.phone_input = 'xpath=//*[@id="mobile_number"]'
        self.create_account_button = 'xpath=//*[@id="form"]/div/div/div/div/form/button'

    def fill_signup_form(self, user_data: dict):
        self.page.click(self.gender_checkbox)
        self.page.fill(self.password_input, user_data["password"])
        self.page.fill(self.first_name_input, user_data["first_name"])
        self.page.fill(self.last_name_input, user_data["last_name"])
        self.page.fill(self.company_input, user_data["company"])
        self.page.fill(self.address_input, user_data["address"])
        self.page.select_option(self.country_dropdown, value=user_data["country"])
        self.page.fill(self.state_input, user_data["state"])
        self.page.fill(self.city_input, user_data["city"])
        self.page.fill(self.zipcode_input, user_data["zipcode"])
        self.page.fill(self.phone_input, user_data["phone"])

    def submit_form(self):
        self.page.click(self.create_account_button)
