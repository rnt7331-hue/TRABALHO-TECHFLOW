# PARECER TÉCNICO — ARQUITETURA DO TECHFLOW CORE

## 1. Comparação entre arquiteturas

**Aplicações Console/CLI:** São executadas por meio de comandos em um terminal. Possuem uma estrutura mais simples, consomem menos recursos computacionais e são adequadas para sistemas que não necessitam de uma interface gráfica elaborada.

**Aplicações Web:** Funcionam por meio de navegadores e permitem que diferentes usuários acessem o sistema pela internet ou rede local. Oferecem maior acessibilidade, porém exigem uma estrutura mais complexa, envolvendo servidores e tecnologias adicionais.

**Aplicações Desktop:** São programas instalados diretamente no computador, geralmente com interfaces gráficas próprias. Proporcionam uma experiência visual mais completa, mas podem exigir mais recursos e manutenção específica para cada sistema operacional.

## 2. Justificativa da escolha

A escolha do Python em modo CLI para o TechFlow Core foi baseada na simplicidade, eficiência e compatibilidade com os requisitos do projeto.

O sistema tem como objetivo principal cadastrar, consultar, atualizar e excluir demandas internas, não necessitando de uma interface gráfica complexa. A arquitetura CLI permite desenvolver essas funcionalidades de maneira organizada e com baixo consumo de recursos.

Além disso, o Python oferece recursos suficientes para implementar as operações necessárias, integrar APIs externas e realizar o tratamento de erros. Portanto, a arquitetura CLI representa uma solução adequada, econômica e eficiente para atender às necessidades do TechFlow Core.