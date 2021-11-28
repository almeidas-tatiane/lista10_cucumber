Feature: Cadastro no site do Blazedemo
  Scenario: Cadastro no site do Blazedemo com informacoes validas em todos os campos
    Given que acesso o  site do Blazedemo
    And clico em home
    When clico em Register
    And preencho os campos 'Tatiane','Iterasys','tatiane@iterasys.com.br','abc123','abc123'
    And clico no botao Register
    Then valido se o cadastro foi efetuado
