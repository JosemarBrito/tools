# Caixa de Ferramentas
____

Modúlo sobre criação de ferramentas para simplificação de testes e correção de falhas no aplicativo

[![Build Status](https://travis-ci.org/JosemarBrito/tools.svg?branch=main)](https://travis-ci.org/JosemarBrito/tools)
# Configuração

1. Chave SSH
2. Pyenv para Isolar ambiente de desenvolvimento
3. Virtualenv, para isolar projeto
4. Configurado virtualenv no Pycharm

# Ferramentas criadas:

API para consulta de [avatar](https://api.github.com/users/JosemarBrito) no Github
1. pip install [requests](https://requests.readthedocs.io/en/master/)
2. criado arquivo python para busca de  avatar no github
____
Requirements: Criado para colocar as dependencias exestentes no ".venv"
>1. pip freeze > requirements.txt
____

#[Flake8](https://flake8.pycqa.org/en/latest/)
>1. pip freeze > requirements-dev.txt

1.a. criar dentro do requirements-dev.txt 
>-r requirements.txt

e apagar as dependencias presentes no requirements que tambem constam no -dev
   
* Para utilizar o flake8, é só digitar na linha de comando que irá reportar fallhas no codigo referente a PEP8

____

#[Travis-CI](https://travis-ci.org/) 
[![Build Status](https://travis-ci.org/JosemarBrito/tools.svg?branch=main)](https://travis-ci.org/JosemarBrito/tools)
____
1. Criar arquivo '.travis.yml'

