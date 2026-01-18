# 🌦️ Consulta de Clima com Python

Este é um projeto prático de **Ciência de Dados** desenvolvido para aplicar conceitos fundamentais de integração de sistemas e visualização de dados. O script consome dados reais via API, processa as informações e gera relatórios visuais automáticos.

## 🎯 Relevância Técnica
Este projeto executa um **ciclo completo de dados (ETL)**, demonstrando competências essenciais para o mercado de dados:

1.  **Integração de Sistemas (API):** Conexão programática com fontes externas (Open-Meteo) para extração de dados em tempo real.
2.  **Tratamento de Dados (Parsing):** Manipulação de estruturas JSON complexas para filtrar e organizar apenas as informações estratégicas.
3.  **Visualização de Dados:** Transformação de dados brutos em inteligência visual (*Data Visualization*) para facilitar a análise de tendências.
4.  **Resiliência e Boas Práticas:** Implementação de tratamento de erros e verificação de status HTTP, garantindo a robustez da aplicação.

## 📝 Funcionalidades
- Recebe a latitude e longitude via `input` do usuário.
- Faz uma requisição GET na API pública da **Open-Meteo**.
- Verifica se a requisição funcionou (tratamento de erros básico).
- Gera um gráfico de linha mostrando a variação da temperatura.
- Exibe o intervalo de datas no título do gráfico.
- Salva o resultado automaticamente como imagem (`.png`) e exibe na tela.

## 💻 Tecnologias e Bibliotecas
Utilizei Python e duas bibliotecas principais:
- **Requests:** Para acessar o endpoint da API e buscar os dados.
- **Matplotlib:** Para plotar o gráfico visualmente.

## ⚙️ Como rodar o projeto

1. Certifique-se de ter o Python instalado.
2. Instale as dependências com o comando no terminal:
pip install requests matplotlib

Digite a latitude e longitude quando for solicitado no terminal.

Exemplo para São Paulo:

Latitude: -23.55

Longitude: -46.63
