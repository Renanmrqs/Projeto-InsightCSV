# InsightCSV 📊

Aplicação web para análise inteligente de arquivos CSV utilizando IA Generativa (Google Gemini).

## 📋 Sobre o Projeto

InsightCSV é uma ferramenta que permite fazer análises automatizadas de dados em arquivos CSV através de linguagem natural. Basta enviar seu arquivo e o sistema utiliza IA para interpretar, resumir e identificar possíveis problemas nos dados.

---

## 📸 Preview

![Demo](\assets\screenshots\demo_insoghtCSV.gif)
![Visualização de Dados](\assets\screenshots\preview_de_dados.png)

---

## 🚀 Funcionalidades

- ✅ Upload de arquivos CSV
- ✅ Análise automática de estrutura e conteúdo
- ✅ Detecção de erros e inconsistências
- ✅ Resumo inteligente dos dados
- ✅ Interface web intuitiva com Streamlit

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **Streamlit** - Interface web
- **LangChain** - Framework para integração com LLMs
- **Google Gemini** - Modelo de IA generativa
- **Pandas** - Manipulação de dados

## ⚙️ Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- Conta Google Cloud com API Gemini ativada

### Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/Renanmrqs/Projeto-InsightCSV.git
cd Projeto-InsightCSV
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**
```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua API key do Google Gemini
# GOOGLE_API_KEY=sua_chave_aqui
```

5. **Execute a aplicação:**
```bash
streamlit run src/main.py
```

6. **Acesse no navegador:**
```
http://localhost:8501
```

## 📖 Como Usar

1. Acesse a aplicação no navegador
2. Clique em "Browse files" e selecione seu arquivo CSV
3. Clique em "Analisar Arquivo"
4. Aguarde a análise da IA
5. Visualize o resumo e possíveis problemas identificados

## ⚠️ Observações Importantes

- O projeto está em fase de estudos e desenvolvimento
- Os arquivos são processados pelo Google Gemini
- Evite enviar dados sensíveis ou confidenciais
- Respeite os limites de uso da API do Gemini

## 📂 Estrutura do Projeto
```
Projeto-InsightCSV/
├── assets/
│   └── screenshots/      # Capturas de tela da aplicação
├── data/                 # Pasta para CSVs de teste (não versionada)
├── docs/                 # Documentação adicional
├── src/
│   └── main.py          # Código principal da aplicação
├── .env                 # Configurações (não versionado)
├── .env.example         # Template de configuração
├── .gitignore          # Arquivos ignorados pelo Git
├── README.md           # Este arquivo
└── requirements.txt    # Dependências do projeto
```

## 🎯 Próximas Melhorias

- [✅] Análises estatísticas mais detalhadas
- [ ] Geração de gráficos automáticos
- [ ] Histórico de análises
- [ ] Exportação de relatórios

## 📧 Contato

**Renan Fernandes Marques**

- LinkedIn: [Renan Fernandes Marques](https://www.linkedin.com/in/renan-fernandes-marques/)
- GitHub: [@Renanmrqs](https://github.com/Renanmrqs)
- Email: renanmarques1923@gmail.com

## 📄 Licença

Este projeto é de código aberto para fins educacionais.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!