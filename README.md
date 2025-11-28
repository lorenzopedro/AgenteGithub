Agente de IA para GitHub 🐙

Este projeto consiste em um Agente de Inteligência Artificial capaz de analisar repositórios do GitHub, listar issues, commits e ler arquivos utilizando a API do GitHub e o modelo Llama 3 (via Groq).

👥 Integrantes do Grupo

Lorenzo Pedro Freitas Silva

🛠️ Tecnologias Utilizadas

Python 3.10+

LangChain (Framework de Agentes)

Groq API (Llama 3)

PyGithub (Conexão com GitHub)

🚀 Como Rodar o Projeto

Clone o repositório:

git clone [https://github.com/seu-usuario/nome-do-repo.git](https://github.com/seu-usuario/nome-do-repo.git)
cd nome-do-repo


Crie o ambiente virtual e instale as dependências:

python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt


Configure as senhas:
Crie um arquivo .env na raiz do projeto e adicione:

GROQ_API_KEY=sua_chave_groq
GITHUB_ACCESS_TOKEN=seu_token_github
GITHUB_REPOSITORY=usuario/repositorio_alvo


Execute o agente:

python app.py


📊 Monitoramento de Tokens

O agente imprime ao final de cada resposta uma estimativa de tokens utilizados, conforme exigido na especificação do trabalho.