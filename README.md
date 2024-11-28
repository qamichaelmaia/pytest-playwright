# Projeto de Automação - Cadastro de Usuário no Automation Exercise

Este projeto realiza a automação do processo de cadastro de um novo usuário no site **Automation Exercise**. A automação é realizada utilizando a biblioteca **Playwright** para interação com o navegador e **Faker** para a geração de dados fictícios, como nome, email, senha, endereço, entre outros.

## Tecnologias Utilizadas

- **Playwright**: Biblioteca para automação de navegação no navegador.
- **Faker**: Biblioteca para gerar dados falsos (como nome, email, etc.).
- **Python**: Linguagem utilizada para escrever o script de automação.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o seguinte instalado:

1. **Python 3.x** - Caso não tenha, baixe e instale a versão mais recente do Python [aqui](https://www.python.org/downloads/).
2. **Playwright** - Biblioteca para automação de navegação no navegador.
3. **Faker** - Biblioteca para gerar dados falsos.

### Instalar as dependências

Instale as dependências necessárias utilizando o `pip`:

```bash
pip install playwright faker
```

### Instalar os navegadores do Playwright: 

```bash
python -m playwright install
```

## Funcionalidade do Teste

O script realiza as seguintes ações:

- Acessa o site de login do Automation Exercise.
- Preenche os campos de cadastro com dados gerados dinamicamente pelo Faker (nome, email, senha, endereço, telefone, etc.).
- Realiza a seleção de gênero e assinatura de newsletter.
- Finaliza o cadastro e verifica se a mensagem "Account Created!" é exibida, confirmando a criação da conta.

### Execução do Teste
Para rodar o teste, execute o seguinte comando:

```bash
pytest
```
