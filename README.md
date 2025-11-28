# 🐙 Agente de IA para GitHub

Este projeto consiste em um Agente de Inteligência Artificial desenvolvido para a disciplina de **Tópicos Especiais**. O agente é capaz de analisar repositórios do GitHub, listar issues, consultar commits e ler arquivos utilizando a API do GitHub e o modelo **Llama 3** (via Groq Cloud).

O sistema utiliza a arquitetura **ReAct (Reasoning + Acting)**, permitindo que a IA "pense" antes de agir e escolha autonomamente qual ferramenta utilizar para responder à pergunta do usuário.

## 👥 Integrantes do Grupo

* Lorenzo Pedro Freitas Silva

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **LangChain:** Framework para orquestração do Agente ReAct.
* **Groq API:** Acesso rápido e gratuito ao modelo Llama 3 (70b).
* **PyGithub:** Biblioteca para conexão direta e segura com a API do GitHub.
* **Dotenv:** Gerenciamento de variáveis de ambiente e segurança.

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar o agente no seu computador.

### 1. Clone o repositório

```bash
git clone [https://github.com/seu-usuario/nome-do-repo.git](https://github.com/seu-usuario/nome-do-repo.git)
cd nome-do-repo
```

### 2. Crie o ambiente virtual

É recomendável usar um ambiente virtual para não conflitar com outras bibliotecas do seu sistema.

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as Chaves de Acesso

Crie um arquivo chamado `.env` na raiz do projeto (onde está o `app.py`) e adicione suas credenciais.

> ⚠️ **Importante:** O arquivo `.env` contém senhas e não deve ser enviado para o GitHub. Ele já está listado no `.gitignore`.

**Conteúdo do arquivo `.env`:**

```env
# Sua chave da Groq Cloud ([https://console.groq.com](https://console.groq.com))
GROQ_API_KEY=gsk_...

# Seu Token Pessoal do GitHub (Classic Token com permissão 'repo')
GITHUB_ACCESS_TOKEN=ghp_...

# O repositório que você quer analisar (Usuario/NomeDoRepo)
GITHUB_REPOSITORY=lorenzopedro/DesenvAvancadoII
```

### 5. Execute o Agente

```bash
python app.py
```

## 🤖 Exemplo de Uso

Após iniciar, você pode fazer perguntas em linguagem natural para o terminal:

* "Quais são as últimas 3 issues abertas?"
* "Quem fez o último commit e o que ele alterou?"
* "Leia o arquivo README.md para mim."
* "Me faça um resumo sobre o que é este repositório."

## 📊 Monitoramento de Tokens

Conforme solicitado nos requisitos do trabalho, o agente exibe ao final de cada resposta uma estimativa da quantidade de tokens utilizados na interação (Input + Output).

```text
🤖: As últimas issues são sobre correção de bugs na API...
📊 Tokens estimados: 156
```

---

**Disciplina:** Tópicos Especiais  
**Professor:** Me. Alexandre Alves  
**Data:** Novembro/2025