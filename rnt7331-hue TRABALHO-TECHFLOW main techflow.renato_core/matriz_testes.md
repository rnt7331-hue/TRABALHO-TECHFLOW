
# TECHFLOW CORE
## ETAPA 12 — MATRIZ DE TESTES E VALIDAÇÃO

**Projeto:** TechFlow Core
**Versão:** Alpha 1.0
**Etapa:** 12 — Matriz de Testes e Validação
**Data:** 26/11/2026

---

## 1. Objetivo

Documentar os testes realizados no TechFlow Core,
verificando o funcionamento das funcionalidades,
a integridade das operações e o tratamento de erros.

## 2. Ambiente de testes

- Linguagem: Python
- Interface: CLI (Terminal)
- Arquitetura: Modular
- Armazenamento: Memória RAM
- Integrações externas: ViaCEP e AwesomeAPI
- Bibliotecas externas: Nenhuma

## 3. Matriz de testes funcionais

| ID | Funcionalidade | Teste realizado | Resultado esperado | Situação |
|---|---|---|---|---|
| T01 | Inicialização | Executar main.py | Menu principal exibido | APROVADO |
| T02 | Cadastro | Cadastrar demanda válida | Demanda registrada | APROVADO |
| T03 | Validação | Informar prioridade inválida | Cadastro impedido | APROVADO |
| T04 | Consulta | Consultar demanda existente | Dados exibidos | APROVADO |
| T05 | Listagem | Listar demandas | Todas as demandas exibidas | APROVADO |
| T06 | Atualização | Alterar status | Novo status registrado | APROVADO |
| T07 | Exclusão | Excluir demanda existente | Demanda removida | APROVADO |
| T08 | Filtro | Filtrar prioridade Alta | Apenas demandas Alta exibidas | APROVADO |
| T09 | CEP | Consultar CEP válido | Endereço retornado | APROVADO |
| T10 | Cotação | Consultar dólar | Cotação retornada | APROVADO |
| T11 | Conversão | Converter BRL para USD | Valor convertido corretamente | APROVADO |
| T12 | Tratamento | Informar ID inválido | Mensagem de erro exibida | APROVADO |

## 4. Testes de integração

| ID | Módulos envolvidos | Verificação | Situação |
|---|---|---|---|
| I01 | main.py + gerenciador_demandas.py | Operações de cadastro e consulta | APROVADO |
| I02 | main.py + utils.py | Formatação e validações | APROVADO |
| I03 | main.py + integracoes_api.py | Comunicação com APIs | APROVADO |
| I04 | Todos os módulos | Execução integrada pelo menu | APROVADO |

## 5. Tratamento de falhas

Foram consideradas as seguintes situações:

- CEP inválido ou inexistente.
- Falha de conexão com serviços externos.
- Cotação do dólar indisponível.
- Identificador inexistente.
- Prioridade inválida.
- Valor monetário inválido.
- Opção inexistente no menu.

O sistema possui mecanismos de validação e tratamento
de exceções para reduzir interrupções inesperadas.

## 6. Limitações conhecidas

- Os dados são armazenados em memória RAM.
- Os registros são perdidos quando o programa é encerrado.
- As consultas externas dependem de conexão com a internet.
- A cotação do dólar pode variar durante o funcionamento.

## 7. Resultado geral

Com base nos testes executados, a Versão Alpha do
TechFlow Core apresentou funcionamento satisfatório
nas funcionalidades verificadas.

A arquitetura modular permitiu integrar os componentes
e executar as operações pelo menu principal.

**Resultado:** TESTES FUNCIONAIS RELATADOS COMO APROVADOS.

---
TECHFLOW CORE — DOCUMENTAÇÃO TÉCNICA
