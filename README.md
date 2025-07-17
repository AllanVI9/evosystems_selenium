### 💼 EvoSystems – Selenium Python Test

## 🎯 Objetivo do Sistema

Esta aplicação tem como objetivo efetuar os testes automatizados para o site https://www.saucedemo.com/ usando a ferramenta Selenium através da linguagem Python.  

## ✅ Pré-requisitos
- selenium >= 4.34
- webdriver-manager >= 4.0
- pytest >= 8.4

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
  O fluxo lógico segue com as seguintes verificações:
  - Se o Login foi efetuado com sucesso.
  - Se a lista de produtos foi exibida.
  - Se os produtos foram adicionados ao carrinho com sucesso.
  - Se os produtos são removidos do carrinho com sucesso.
  - Se ao clicar no botão "Checkout" somos direcionados para a tela de passo 1 do checkout.
  - Se os campos na tela do passo 1 do checkout são preenchidos com sucesso.
  - Se ao clicar no botão "Continue" da tela do passo 1 do checkout somos direcionados para a tela do passo 2.
  - Se ao clicar no botão "Finish" da tela do passo 2 do checkout somos direcionados para a tela de compra finalizada.
  - Se a tela de compra finalizada sempre exibe a mensagem de checkout completado com sucesso.

  O teste tenta fazer login com cada usuário e verificar se o login foi bem-sucedido ou falhou, tratando erros adequadamente.
