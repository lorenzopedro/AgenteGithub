import os
from dotenv import load_dotenv
from github import Github, Auth
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain.tools import tool

# 1. Carregar Variáveis
load_dotenv()

# 2. Configuração GitHub
GITHUB_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")

if not GITHUB_TOKEN or not REPO_NAME:
    print("❌ ERRO: Token ou Repo faltando no .env")
    exit(1)

try:
    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    repo = g.get_repo(REPO_NAME)
    print(f"✅ Conectado ao repo: {repo.full_name}")
except Exception as e:
    print(f"❌ Erro GitHub: {e}")
    exit(1)

# 3. DEFINIÇÃO DAS FERRAMENTAS

@tool
def listar_issues(quantidade: str = "5"):
    """Lista as últimas issues abertas. Entrada: número de issues (ex: '5')."""
    try:
        qtd = int(quantidade) if quantidade.isdigit() else 5
        issues = repo.get_issues(state='open')[:qtd]
        if not list(issues):
            return "Nenhuma issue aberta encontrada."
        
        resultado = []
        for issue in issues:
            resultado.append(f"Issue #{issue.number}: {issue.title} (Autor: {issue.user.login})")
        return "\n".join(resultado)
    except Exception as e:
        return f"Erro: {str(e)}"

@tool
def listar_commits(quantidade: str = "5"):
    """Lista os últimos commits. Entrada: número de commits (ex: '3')."""
    try:
        qtd = int(quantidade) if quantidade.isdigit() else 5
        commits = repo.get_commits()[:qtd]
        resultado = []
        for c in commits:
            msg = c.commit.message.split('\n')[0]
            resultado.append(f"[{c.sha[:7]}] {c.commit.author.name}: {msg}")
        return "\n".join(resultado)
    except Exception as e:
        return f"Erro: {str(e)}"

@tool
def ler_arquivo(caminho: str):
    """Lê o conteúdo de um arquivo. Entrada: caminho do arquivo (ex: 'README.md')."""
    try:
        contents = repo.get_contents(caminho)
        return contents.decoded_content.decode("utf-8")
    except Exception as e:
        return f"Erro ao ler '{caminho}': {str(e)}"

@tool
def info_geral(query: str = ""):
    """Retorna informações gerais do repositório (descrição, linguagem, estrelas)."""
    return f"Repo: {repo.full_name}\nLinguagem: {repo.language}\nEstrelas: {repo.stargazers_count}\nDescrição: {repo.description}"

minhas_tools = [listar_issues, listar_commits, ler_arquivo, info_geral]

def main():
    print("🐙 --- AGENTE GITHUB (Versão ReAct) ---")
    
    if not os.getenv("GROQ_API_KEY"):
        print("❌ Chave GROQ não encontrada.")
        return

    # 4. LLM
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    # 5. Prompt ReAct (O Cérebro em Texto Puro)
    # Este template ensina o robô a pensar passo-a-passo
    template = """Responda as perguntas do usuário da melhor forma possível. 
Você tem acesso às seguintes ferramentas:

{tools}

Use o seguinte formato:

Question: a pergunta que você deve responder
Thought: você deve sempre pensar sobre o que fazer
Action: a ação a ser tomada, deve ser uma de [{tool_names}]
Action Input: a entrada para a ação
Observation: o resultado da ação
... (este ciclo Thought/Action/Action Input/Observation pode repetir N vezes)
Thought: Agora eu sei a resposta final
Final Answer: a resposta final para a pergunta original (em Português)

Begin!

Question: {input}
Thought:{agent_scratchpad}"""

    prompt = PromptTemplate.from_template(template)

    # 6. Criar Agente ReAct
    agent = create_react_agent(llm, minhas_tools, prompt)
    
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=minhas_tools, 
        verbose=True, 
        handle_parsing_errors=True
    )

    print("\n✅ AGENTE PRONTO! Digite sua pergunta.")
    print("---------------------------------------")

    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() in ["sair", "fim", "exit"]:
            break

        try:
            print("⏳ Pensando...")
            res = agent_executor.invoke({"input": pergunta})
            print(f"\n🤖: {res['output']}")
            
            # Monitoramento Simples
            tokens = (len(pergunta) + len(res['output'])) // 4
            print(f"📊 Tokens estimados: {tokens}")

        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()