# Projeto de Automação - Cadastro de Usuário no Automation Exercise

Este projeto realiza a automação do processo de cadastro de um novo usuário no site **Automation Exercise**. A automação é realizada utilizando a biblioteca **Playwright** para interação com o navegador e **Faker** para a geração de dados fictícios, como nome, email, senha, endereço, entre outros. Também foi utilizado **Page Objects** para deixar os testes mais dinâmicos.


## Tecnologias Utilizadas (Pré-requisitos)
Antes de rodar o projeto, certifique-se de ter o seguinte instalado:

- **Python**: Linguagem utilizada para escrever o script de automação[Download](https://www.python.org/downloads/).
- **Playwright**: Biblioteca para automação de navegação no navegador [Documentação](https://playwright.dev/python/docs/intro).
- **Faker**: Biblioteca para gerar dados falsos (como nome, email, etc.)[Documentação](https://faker.readthedocs.io/en/master/).
- **Page Objects**: Formato dinâmico para os testes [Documentação](https://playwright.dev/python/docs/pom).


## Funcionalidade do Teste

O script realiza as seguintes ações:

- Acessa o site de login do Automation Exercise.
- Preenche os campos de cadastro com dados gerados dinamicamente pelo Faker (nome, email, senha, endereço, telefone, etc.).
- Realiza a seleção de gênero e assinatura de newsletter.
- Finaliza o cadastro e verifica se a mensagem "Account Created!" é exibida, confirmando a criação da conta.


### Instalar as dependências

Instale as dependências necessárias utilizando o `pip`:

```bash
pip install playwright faker
```

### Instalar os navegadores do Playwright: 

```bash
python -m playwright install
```


### Execução do Teste
Para rodar o teste, execute o seguinte comando:

```bash
pytest
```
