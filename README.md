### 💼 EvoSystems – Selenium Python Test

## 🎯 Objetivo do Sistema

Esta aplicação tem como objetivo efetuar os testes automatizados para o site https://www.saucedemo.com/ usando a ferramenta Selenium através da linguagem Python.

## ✅ Pré-requisitos
- selenium >= 4.34
- webdriver-manager >= 4.0
- pytest >= 8.4
- pytest-html

## 💻 Instalação via Windows

### 1. 📦 Criar um ambiente virtual (recomendado)

    python -m venv venv

### 2. 🔹 Ativar o ambiente virtual
    venv\Scripts\activate

### 3. 🚀 Instalar as dependências

    pip install selenium

    pip install webdriver-manager

    pip install pytest

    pip install pytest-html

  ou de uma vez...

    pip install selenium webdriver_manager pytest pytest-html

  ou via requirements...

    pip install -r requirements.txt

### 4. ▶️ Executar script de teste
- Para executar um teste espeífico:

  Ex:
  ```python
  pytest ./tests/test_login.py

- Para executar um teste espeífico com mais detalhes:

  Ex:
  ```python
  pytest ./tests/test_login.py -s -v

- Para executar um teste espeífico com geração de relatório:

  Ex:
  ```python
  pytest ./tests/test_login.py --html=report.html

- Para executar todos os testes:

  Ex:
  ```python
  pytest

- Para executar todos os testes com mais detalhes:

  Ex:
  ```python
  pytest -v

- Para executar todos os testes com geração de relatórios:

  Ex:
  ```python
  pytest --html=report.html

### 🧾 Cenários cobertos:
 - Login
 - Adição de Produtos
 - Remoção de Produtos
 - Checkout – Etapa 1: Filtragem de Campos
 - Checkout – Etapa 2: Avançar para próxima etapa, caso todos os campos sejam preenchidos corretamente
 - Checkout – Etapa 3: Finalização do checkout e conclusão da compra

### 🗺️ O que o código faz e seu fluxo:

#### O teste pode ser executado de forma total (aleatório) ou de forma individual.

#### O fluxo lógico segue com as seguintes verificações:

#### 🧪 test_login

  - Carregar o setup da pagina de Login onde ocorrem as seguintes ações:
    - Preencher os campos de 'username' e 'password'.
    - Clicar no botão 'Login'.

  - Verificar se o login ocorreu com sucesso.
  - Verificar se a lista de produtos está visível.
  - Efetuar o logout e reset do ambiente.

#### 🧪 test_cart_add

  - Carregar o setup da pagina de Login onde ocorrem as seguintes ações:
    - Preencher os campos de 'username' e 'password'.
    - Clicar no botão 'Login'.

  - Carregar o setup da pagina de Produtos onde ocorrem as seguintes ações:
    - Varrer a lista de produtos e adicionar os mesmos ao carrinho.

  - Verificar se a quantidade adicionada ao carrinho bate as do ícone totalizador do carrinho.
  - Verificar se os nomes dos produtos exibidos no carrinho batem com os adicionados ao mesmo.
  - Efetuar o logout e reset do ambiente.

#### 🧪 test_cart_remove

  - Carregar o setup da pagina de Login onde ocorrem as seguintes ações:
    - Preencher os campos de 'username' e 'password'.
    - Clicar no botão 'Login'.

  - Carregar o setup da pagina de Produtos onde ocorrem as seguintes ações:
    - Varrer a lista de produtos e adicionar os mesmos ao carrinho.
    - Executar um looping para remover todos os produtos do carrinho

  - Verificar se o total de produtos adicionados foi removido.
  - Verificar se o ícone totalizador do carrinho não está mais visível após a remoção de todos os produtos.
  - Efetuar o logout e reset do ambiente.

#### 🧪 test_checkout_step_1_fill_fields

  - Carregar o setup da pagina de Login onde ocorrem as seguintes ações:
    - Preencher os campos de 'username' e 'password'.
    - Clicar no botão 'Login'.

  - Carregar o setup da pagina de Produtos onde ocorrem as seguintes ações:
    - Varrer a lista de produtos e adicionar os mesmos ao carrinho.

  - Carregar o setup do Checkout.

  - Verificar se ao clicar no botão 'Continue' as mensagens de erro referente aos campos não preenchidos são exibidas.
  - Efetuar o logout e reset do ambiente.

#### 🧪 test_checkout_step_2_next

  - Carregar o setup da pagina de Login onde ocorrem as seguintes ações:
    - Preencher os campos de 'username' e 'password'.
    - Clicar no botão 'Login'.

  - Carregar o setup da pagina de Produtos onde ocorrem as seguintes ações:
    - Varrer a lista de produtos e adicionar os mesmos ao carrinho.

  - Carregar o setup do Checkout.

  - Verificar se ao clicar no botão 'Continue' todos os campos foram preenchidos
  - Verificar se houve o avanço para próxima página de checkout
  - Efetuar o logout e reset do ambiente.

#### 🧪 test_checkout_step_3_finish

  - Carregar o setup da pagina de Login onde ocorrem as seguintes ações:
    - Preencher os campos de 'username' e 'password'.
    - Clicar no botão 'Login'.

  - Carregar o setup da pagina de Produtos onde ocorrem as seguintes ações:
    - Varrer a lista de produtos e adicionar os mesmos ao carrinho.

  - Carregar o setup do Checkout.

  - Verificar o sucesso da compra
  - Efetuar o logout e reset do ambiente.
