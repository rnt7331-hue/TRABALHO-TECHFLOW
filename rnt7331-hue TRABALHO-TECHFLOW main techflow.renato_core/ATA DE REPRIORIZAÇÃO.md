# ATA DE REPRIORIZAÇÃO DE ESCOPO — TECHFLOW CORE

1. A reunião foi realizada entre a equipe de desenvolvimento e a Diretoria Comercial da TechFlow Solutions.
2. A Diretoria solicitou a inclusão do campo `valor_estimado_brl` no cadastro de demandas.
3. Ficou acordado que o sistema realizará a conversão automática do valor em reais para dólares utilizando a cotação da AwesomeAPI.
4. Também foi aprovada a implementação de um filtro de listagem por prioridade: Alta, Média e Baixa.
5. A equipe manterá a arquitetura CLI em Python, evitando uma migração Web nesta etapa.
6. O módulo `integracoes_api.py` será reaproveitado para consultar a cotação do dólar.
7. Serão aplicados tratamentos de exceção para evitar falhas quando não houver conexão com a internet.
8. A implementação será realizada sem comprometer as funcionalidades existentes do sistema.
9. A utilização do SQLite será considerada uma melhoria opcional, conforme disponibilidade de tempo.
10. A Diretoria aprovou a repriorização, mantendo a data final de entrega em 08/12.