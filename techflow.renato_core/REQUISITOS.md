# REQUISITOS DO SISTEMA — TECHFLOW CORE

## 1. Descrição do Projeto

O TechFlow Core é um sistema de gerenciamento de demandas e chamados técnicos, desenvolvido em Python e executado por meio de uma interface de linha de comando (CLI).

Seu objetivo é facilitar o cadastro, a organização, a consulta e o acompanhamento de demandas internas.

## 2. Requisitos Funcionais (RF)

**RF01 — Cadastrar demandas:** O sistema deverá permitir cadastrar novas demandas, contendo ID, título, solicitante, prioridade, CEP, cidade e status.

**RF02 — Listar demandas:** O sistema deverá apresentar todas as demandas cadastradas, permitindo visualizar suas informações.

**RF03 — Buscar demandas:** O sistema deverá permitir localizar uma demanda específica por meio do seu ID.

**RF04 — Atualizar status:** O sistema deverá permitir modificar o status de uma demanda cadastrada.

**RF05 — Excluir demandas:** O sistema deverá permitir remover uma demanda existente por meio do seu ID.

**RF06 — Consultar CEP e cotação:** O sistema deverá permitir consultar informações de endereço por meio da API ViaCEP e consultar a cotação do dólar por meio da AwesomeAPI.

## 3. Requisitos Não Funcionais (RNF)

**RNF01 — Segurança:** O sistema deverá validar as informações fornecidas pelo usuário e tratar possíveis erros durante a execução.

**RNF02 — Integridade:** O sistema deverá impedir cadastros com campos obrigatórios vazios e IDs duplicados.

**RNF03 — Usabilidade:** A interface deverá apresentar menus organizados e mensagens claras para facilitar a utilização.

**RNF04 — Desempenho:** O sistema deverá executar operações de cadastro, consulta, atualização e exclusão de maneira rápida.

**RNF05 — Confiabilidade:** O sistema deverá continuar funcionando mesmo quando ocorrerem entradas inválidas ou falhas nas conexões com APIs externas.

## 4. Tecnologias Utilizadas

- Linguagem: Python 3.
- Interface: CLI (Linha de Comando).
- Editor: Visual Studio Code.
- APIs externas: ViaCEP e AwesomeAPI.
- Formato de dados: JSON.

## 5. Objetivo Final

Entregar um sistema funcional, organizado, seguro e capaz de gerenciar demandas internas, integrando consultas externas e oferecendo uma experiência simples ao usuário.