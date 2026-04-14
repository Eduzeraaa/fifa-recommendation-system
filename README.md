# 🇧🇷 Sistema de Análise e Recomendação de Jogadores (FIFA 23)

## 📌 Descrição
O Sistema de Análise e Recomendação de Jogadores é uma aplicação interativa que combina análise de dados com inteligência artificial para auxiliar na tomada de decisão em contratações no futebol.

A aplicação utiliza um dataset do FIFA 23, junto com técnicas de análise de dados (Pandas, Matplotlib) e um chatbot com LLM para recomendar jogadores com base em critérios como orçamento, posição, idade e potencial.

O sistema interpreta a mensagem do usuário, filtra os dados em tempo real e utiliza a IA para sugerir as melhores opções de contratação de forma explicativa.

---

## ⚙️ Funcionalidades

- Dashboard interativo com análise de jogadores
- Visualização por faixa de overall
- Top jogadores por:
  - Valor de mercado
  - Overall
- Melhores jogadores por posição:
  - Goleiros, zagueiros, laterais, meio-campistas e atacantes
- Identificação de melhores promessas:
  - Geral
  - Por ganho de overall (potencial - overall)
- Sistema de recomendação via chatbot
- Filtro automático por:
  - Orçamento
  - Posição
- Sugestão inteligente de jogadores

---

## 🧠 Diferenciais Técnicos

- Integração de análise de dados com IA
- Sistema de recomendação baseado em score personalizado
- Conversão de dados brutos em decisões inteligentes
- Pipeline completo:
  - Entrada do usuário → processamento → recomendação
- Uso de LLM para explicação e tomada de decisão
- Tratamento e limpeza de dados reais (dataset com inconsistências)
- Separação clara entre lógica (Python) e interpretação (LLM)

---

## 🏗️ Arquitetura

Fluxo principal:

1. Usuário envia mensagem no chatbot
2. Parser extrai:
   - Orçamento
   - Posição desejada
3. Sistema filtra o dataset:
   - Remove jogadores irrelevantes (RES/SUB)
   - Filtra por posição
   - Filtra por valor
4. Sistema calcula e ordena por score
5. Top jogadores são convertidos em texto
6. LLM recebe:
   - Pergunta do usuário
   - Lista de jogadores filtrados
7. IA recomenda os melhores jogadores com explicação

---

## 🛠️ Tecnologias

- Python
- Streamlit
- Pandas
- LangChain
- LLM (via API)

---

## 🧪 Aprendizados do Projeto

- Manipulação e análise de dados com Pandas
- Criação de dashboards interativos com Streamlit
- Limpeza e tratamento de dados reais
- Construção de sistemas de recomendação
- Integração de LLM com aplicações reais
- Engenharia de prompts
- Separação de responsabilidades entre backend e IA
- Debugging de erros comuns em Data Science

---

## 🚀 Próximos Passos

- Melhorar o parser (idade, preferências, múltiplas posições)
- Implementar sistema de múltiplas recomendações (ex: 2 jogadores)
- Adicionar filtros avançados (liga, nacionalidade, clube)
- Melhorar UI/UX do chatbot
- Comparação entre jogadores

---

# 🇺🇸 Player Analysis and Recommendation System (FIFA 23)

## 📌 Description
The Player Analysis and Recommendation System is an interactive application that combines data analysis with artificial intelligence to support decision-making in football player recruitment.

The application uses a FIFA 23 dataset along with data analysis techniques (Pandas, Matplotlib) and an LLM-powered chatbot to recommend players based on criteria such as budget, position, age, and potential.

The system interprets user messages, filters data in real time, and uses AI to suggest the best signing options with clear explanations.

---

## ⚙️ Features

- Interactive dashboard for player analysis
- Overall rating distribution visualization
- Top players by:
  - Market value
  - Overall rating
- Best players by position:
  - Goalkeepers, defenders, full-backs, midfielders, and forwards
- Identification of top prospects:
  - Overall
  - By overall growth (potential - overall)
- Chatbot-based recommendation system
- Automatic filtering by:
  - Budget
  - Position
- Intelligent player suggestions

---

## 🧠 Technical Highlights

- Integration of data analysis with AI
- Custom score-based recommendation system
- Transformation of raw data into intelligent decisions
- Complete pipeline:
  - User input → processing → recommendation
- Use of LLM for explanation and decision-making
- Real-world data cleaning and preprocessing
- Clear separation between logic (Python) and reasoning (LLM)

---

## 🏗️ Architecture

Main flow:

1. User sends a message in the chatbot
2. Parser extracts:
   - Budget
   - Desired position
3. System filters the dataset:
   - Removes irrelevant players (RES/SUB)
   - Filters by position
   - Filters by value
4. System calculates and ranks players by score
5. Top players are converted into text
6. LLM receives:
   - User question
   - Filtered player list
7. AI recommends the best players with explanation

---

## 🛠️ Technologies

- Python
- Streamlit
- Pandas
- LangChain
- LLM (via API)

---

## 🧪 Project Learnings

- Data manipulation and analysis with Pandas
- Building interactive dashboards with Streamlit
- Cleaning and handling real-world datasets
- Designing recommendation systems
- Integrating LLM into real applications
- Prompt engineering
- Separation of concerns between backend and AI
- Debugging common data science issues

---

## 🚀 Next Steps

- Improve parser (age, preferences, multiple positions)
- Implement multi-player recommendations (e.g., 2 players)
- Add advanced filters (league, nationality, club)
- Improve chatbot UI/UX
- Player comparison feature
