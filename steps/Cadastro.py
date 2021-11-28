from behave import *

@given('que acesso o  site do Blazedemo')
def que_acesso_o_site_do_Blazedemo(context):
    print('Passo 1- Abre o site')

@given('clico em home')
def clico_em_home(context):
    print('Passo 2- Abre a página de Login')

@when('clico em Register')
def clico_em_Register(context):
    print('Passo 3- Abre a página de Cadastro')

@when('preencho os campos {name}, {company}, {e-mail address}, {password}, {confirm password}')
def preencho_os_campos_name_company_e_mail_address_password_confirm_password(context, name, company, e_mail_address, password, confirm_password):
    print(f'Passo 4- Preenchendo campos do cadastro: {name},{company},{e_mail_address},{password},{confirm_password}')

@when('clico no botao Register')
def clico_no_botao_Register(context):
    print('Passo 5- Enviando informações do cadastro')

@then('valido se o cadastro foi efetuado')
def valido_se_o_cadastro_foi_efetuado(context):
    print('Passo 6- Validação cadastro')