from playwright.sync_api import sync_playwright
from faker import Faker
import time

faker = Faker()

def test_automation_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # abre o navegador em modo headless
        page = browser.new_page()
        page.goto("https://automationexercise.com/login")

        email = faker.email()
        nome = faker.name()
        sobrenome = faker.last_name()               
        senha = faker.password()
        empresa = faker.company()                  
        endereco = faker.address().replace("\n", ", ") 

        #dados cadastro nome/email
        page.locator('xpath=//*[@id="form"]/div/div/div[3]/div/form/input[2]').click() # importante usar sempre aspas símples '' pois alguns xpath contém aspas duplas ""
        page.fill('xpath=//*[@id="form"]/div/div/div[3]/div/form/input[2]', nome )
        page.locator('xpath=//*[@id="form"]/div/div/div[3]/div/form/input[3]').click()
        page.fill('xpath=//*[@id="form"]/div/div/div[3]/div/form/input[3]', email )
        #sign up
        page.locator('xpath=//*[@id="form"]/div/div/div[3]/div/form/button').click()
        time.sleep(8) # espera 5 sec 
        
        #checkbox
        page.locator('xpath=//*[@id="id_gender1"]').click()

        #password
        page.locator('xpath=//*[@id="password"]').click()
        page.fill('xpath=//*[@id="password"]', senha )
        #data de nascimento
        page.locator('//*[@id="days"]').select_option(value='24')
        page.locator('//*[@id="months"]').select_option(value='April')
        page.locator('//*[@id="years"]').select_option(value='1996')

        #assinatura
        page.locator('xpath=//*[@id="newsletter"]').click()
        page.locator('xpath=//*[@id="optin"]').click()

        #primeiro nome
        page.locator('xpath=//*[@id="first_name"]').click()
        page.fill('xpath=//*[@id="first_name"]', nome )

        #sobrenome
        page.locator('xpath=//*[@id="last_name"]').click()
        page.fill('xpath=//*[@id="last_name"]', sobrenome )

        #empresa
        page.locator('xpath=//*[@id="company"]').click()
        page.fill('xpath=//*[@id="company"]', empresa )

        #endereço
        page.locator('xpath=//*[@id="address1"]').click()
        page.fill('xpath=//*[@id="address1"]', endereco )

        #localidade
        page.locator('//*[@id="country"]').select_option(value='Canada') #país
        page.locator('xpath=//*[@id="state"]').click() #estado
        page.fill('xpath=//*[@id="state"]', 'Alberta')
    
        page.locator('xpath=//*[@id="city"]').click() #cidade
        page.fill('xpath=//*[@id="city"]', 'Banff')

        page.locator('xpath=//*[@id="zipcode"]').click() #cep
        page.fill('xpath=//*[@id="zipcode"]', 'T3G 1N4')

        #phone
        page.locator('xpath=//*[@id="mobile_number"]').click()
        page.fill('xpath=//*[@id="mobile_number"]', '999777887')

        #finalizar cadastro
        page.locator('xpath=//*[@id="form"]/div/div/div/div/form/button').click()

        # Obter o texto da mensagem de confirmação
        mensagem = page.locator('//*[@id="form"]/div/div/div/h2/b').text_content()
        assert mensagem == "Account Created!", f"Erro: Esperado 'Account Created!', mas obteve '{mensagem}'"

        time.sleep(8) # espera 5 sec 

        browser.close()