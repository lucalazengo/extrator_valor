#  🚀 Extrator de Valores Monetários com Flask
---

## 📝  Descrição do Projeto

Este projeto é uma aplicação Flask para extração automática de valores monetários de textos, utilizando expressões regulares (Regex) e o modelo de linguagem spaCy para segmentação de sentenças e identificação de entidades nomeadas.

A aplicação permite:
✅ Extrair valores no formato brasileiro (R$ 1.000,00)
✅ Exibir o contexto próximo ao valor encontrado
✅ Identificar entidades nomeadas como pessoas, empresas e locais
✅ Interface amigável e responsiva com HTML, CSS e JS
✅ Deploy com Docker para ambiente de produção

---

# 🚀 Extrator de Valores Monetários com Flask

## 🏆 Tecnologias Utilizadas  

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| ![Python](https://img.shields.io/badge/Python-3.9-blue) | 3.9+ | Linguagem de programação principal |
| ![Flask](https://img.shields.io/badge/Flask-2.0.2-blue) | 2.0.2 | Framework web |
| ![spaCy](https://img.shields.io/badge/spaCy-3.4.1-green) | 3.4.1 | Processamento de linguagem natural |
| ![Regex](https://img.shields.io/badge/Regex-✓-orange) | - | Expressões regulares para extração de valores |
| ![HTML](https://img.shields.io/badge/HTML-5-orange) | - | Interface frontend |
| ![CSS](https://img.shields.io/badge/CSS-3-blue) | - | Estilização frontend |
| ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow) | - | Lógica frontend |
| ![Docker](https://img.shields.io/badge/Docker-20.10.8-blue) | 20.10.8 | Containerização e deploy |

---


---
```
 ## 📂 Estrutura de Diretórios

📂 extract_valor
├── 📂 app
│   ├── 📂 static               # Arquivos CSS e JS
│   ├── 📂 templates            # Arquivos HTML (Jinja2)
│   ├── 📄 __init__.py          # Inicialização do app Flask
│   ├── 📄 routes.py            # Definição das rotas Flask
│   ├── 📄 extract_b.py         # Lógica de extração de valores
├── 📄 Dockerfile               # Configuração Docker
├── 📄 docker-compose.yml       # Configuração Docker Compose
├── 📄 requirements.txt         # Lista de dependências
├── 📄 README.md                # Documentação

```
---

## 🚀 Instalação e Configuração

 1. Clone o Repositório
 2. Crie o Ambiente Virtual (Opcional)
 3. Instale as Dependências

`pip install -r requirements.txt`

 4. Baixe o Modelo spaCy

  `python -m spacy download pt_core_news_sm`

 `python -m nltk.downloader punkt`
 5. Execute o Projeto
`python run.py`

---