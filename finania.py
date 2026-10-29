
import streamlit as st
import requests
import uuid
import json

# =========================================================
# FINAN.IA | ASSISTENTE FINANCEIRO INTELIGENTE
# =========================================================

st.set_page_config(
    page_title="Finan.IA",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

WEBHOOK_URL = (
    "https://n8nserver.appmake.com.br/webhook/"
    "9466375d-ef25-428c-ae68-4f77101686bb"
)

USUARIO_ID = "aluno01"

# =========================================================
# ESTILO VISUAL
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #0b1020;
    --panel: #151f34;
    --border: #2b3958;
    --text: #f0f4ff;
    --muted: #a0aecb;
    --purple: #8b5cf6;
    --cyan: #38bdf8;
    --green: #34d399;
    --red: #fb7185;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 0%, #29204f 0%, transparent 38%),
        radial-gradient(ellipse at 100% 10%, #10384b 0%, transparent 34%),
        var(--bg);
    color: var(--text);
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #11182b, #0d1424);
    border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] * {
    color: var(--text);
}

.brand {
    padding: 16px 10px 24px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 20px;
}

.brand-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    border-radius: 15px;
    background: linear-gradient(135deg, var(--purple), var(--cyan));
    font-size: 23px;
    margin-bottom: 12px;
    box-shadow: 0 7px 25px #8b5cf644;
}

.brand-name {
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -1px;
}

.brand-subtitle {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.7;
    margin-top: 5px;
}

.eyebrow {
    color: var(--cyan);
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 10px;
}

.main-title {
    color: #f6f7ff;
    font-size: clamp(30px, 4vw, 43px);
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.15;
}

.description {
    color: #a7b3d0;
    font-size: 14px;
    line-height: 1.8;
    max-width: 720px;
    margin-top: 12px;
}

.status {
    display: inline-block;
    background: #12372f;
    color: #72f0c0;
    border: 1px solid #236b56;
    padding: 9px 13px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
}

.hero {
    background: linear-gradient(115deg, #35266b, #25245d 46%, #123c56);
    border: 1px solid #51478b;
    border-radius: 22px;
    padding: 27px;
    margin: 26px 0;
    box-shadow: 0 18px 45px #05081666;
}

.hero-label {
    color: #c7b9ff;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.8px;
    margin-bottom: 10px;
}

.hero-title {
    color: white;
    font-size: 23px;
    font-weight: 800;
    margin-bottom: 9px;
}

.hero-text {
    color: #d5d9f5;
    font-size: 13px;
    line-height: 1.8;
}

.section-title {
    color: #edf1ff;
    font-size: 16px;
    font-weight: 800;
    margin: 24px 0 14px;
}

.metric-card {
    background: linear-gradient(145deg, #18233b, #111a2d);
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 20px;
    min-height: 130px;
    box-shadow: 0 8px 24px #05081633;
}

.metric-label {
    color: #9baaca;
    font-size: 12px;
    margin-bottom: 14px;
}

.metric-value {
    color: #f3f5ff;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 8px;
}

.metric-note {
    color: #8f9dbc;
    font-size: 11px;
    line-height: 1.7;
}

.chat-panel {
    background: #141e33;
    border: 1px solid #2a3857;
    border-radius: 16px;
    padding: 17px 20px;
    margin-top: 28px;
    margin-bottom: 15px;
}

.chat-title {
    font-size: 15px;
    font-weight: 800;
    color: #f2f5ff;
}

.chat-subtitle {
    color: #93a2c3;
    font-size: 11px;
    margin-top: 5px;
}

div[data-testid="stChatMessage"] {
    border: 1px solid #293653;
    border-radius: 18px;
    padding: 15px 17px;
    margin: 12px 0;
    background: #151f34;
    box-shadow: 0 6px 20px #05081622;
}

div[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) {
    background: linear-gradient(135deg, #292452, #202344);
    border-color: #51458b;
}

div[data-testid="stChatMessage"] p {
    color: #eef2ff;
    font-size: 14px;
    line-height: 1.8;
}

div[data-testid="stChatMessage"] strong {
    color: #8ee7ff;
}

div[data-testid="stChatInput"] {
    background: #151f34;
    border: 1px solid #384768;
    border-radius: 17px;
}

div[data-testid="stChatInput"] textarea {
    color: #f5f7ff !important;
    caret-color: var(--cyan);
}

div[data-testid="stChatInput"] textarea::placeholder {
    color: #a5b1ca !important;
}

.stButton > button {
    background: linear-gradient(135deg, #7548dd, #426de0);
    color: white;
    border: 1px solid #8069e9;
    border-radius: 12px;
    min-height: 42px;
    font-weight: 700;
}

.stButton > button:hover {
    border-color: #73d8ff;
    color: white;
}

.footer {
    border-top: 1px solid #283654;
    padding-top: 17px;
    margin-top: 30px;
    color: #a0aecb;
    text-align: center;
    font-size: 11px;
    line-height: 1.8;
}

@media (max-width: 700px) {
    .block-container {
        padding: 1rem 1rem 2rem;
    }
    .hero {
        padding: 20px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================

def extrair_resposta(dados):
    """Localiza o texto da resposta em formatos comuns do n8n."""

    if isinstance(dados, str):
        texto = dados.strip()

        # Tenta interpretar JSON que tenha vindo como texto.
        if texto.startswith("{") or texto.startswith("["):
            try:
                convertido = json.loads(texto)
                if isinstance(convertido, (dict, list)):
                    return extrair_resposta(convertido)
            except (ValueError, TypeError):
                pass

        return texto or None

    if isinstance(dados, list):
        for item in dados:
            resultado = extrair_resposta(item)
            if resultado:
                return resultado
        return None

    if isinstance(dados, dict):
        # Primeiro procura campos que normalmente contêm a resposta.
        chaves = (
            "resposta",
            "output",
            "text",
            "response",
            "answer",
            "message",
        )

        for chave in chaves:
            valor = dados.get(chave)

            if isinstance(valor, str) and valor.strip():
                return valor.strip()

            if isinstance(valor, (dict, list)):
                resultado = extrair_resposta(valor)
                if resultado:
                    return resultado

        # Depois verifica estruturas aninhadas.
        for chave in ("data", "result", "body"):
            valor = dados.get(chave)

            if isinstance(valor, (dict, list)):
                resultado = extrair_resposta(valor)
                if resultado:
                    return resultado

    return None


def consultar_n8n(pergunta):
    """Envia a mensagem ao webhook e devolve a resposta."""

    payload = {
        "chatInput": pergunta,
        "usuario_id": USUARIO_ID,
        "sessionId": st.session_state.session_id,
    }

    resposta_http = requests.post(
        WEBHOOK_URL,
        json=payload,
        timeout=90,
    )

    resposta_http.raise_for_status()

    try:
        dados = resposta_http.json()
    except ValueError:
        dados = resposta_http.text

    texto = extrair_resposta(dados)

    if texto:
        return texto

    # Ajuda a diagnosticar respostas com formato inesperado.
    return (
        "O n8n respondeu, mas não encontrei um texto para exibir.\n\n"
        "Confira a saída do nó AI Agent e a configuração do "
        "Respond to Webhook."
    )


# =========================================================
# INICIALIZAÇÃO DO HISTÓRICO
# =========================================================

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá! Sou o assistente do Finan.IA. 💜\n\n"
                "Posso ajudar a registrar despesas e receitas, "
                "além de consultar informações financeiras "
                "disponíveis no sistema.\n\n"
                "O que deseja fazer hoje?"
            ),
        }
    ]

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())


# =========================================================
# BARRA LATERAL
# =========================================================

with st.sidebar:
    st.markdown("""
    <div class="brand">
        <div class="brand-icon">💰</div>
        <div class="brand-name">Finan.IA</div>
        <div class="brand-subtitle">
            Seu espaço de organização financeira
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.caption("SEU ASSISTENTE")

    st.markdown("""
    **Conversa financeira**

    Registre movimentações e converse com o assistente
    usando mensagens simples.

    ---

    **O que você pode fazer**

    - Registrar despesas
    - Registrar receitas
    - Consultar movimentações
    - Perguntar sobre seu saldo
    """)
    
    st.markdown("---")
    st.caption(f"Usuário conectado: {USUARIO_ID}")

    if st.button("Nova conversa", use_container_width=True):
        st.session_state.mensagens = [
            {
                "role": "assistant",
                "content": (
                    "Nova conversa iniciada. "
                    "Como posso ajudar com suas finanças?"
                ),
            }
        ]
        st.session_state.session_id = str(uuid.uuid4())
        st.rerun()

    st.markdown("""
    <div class="footer">
        Finan.IA<br>
        Organização financeira inteligente
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# CABEÇALHO PRINCIPAL
# =========================================================

st.markdown("""
<div>
    <div class="eyebrow">Assistente financeiro inteligente</div>
    <div class="main-title">Suas finanças,<br>em uma conversa.</div>
    <div class="description">
        Registre despesas, informe receitas e converse com o
        Finan.IA para organizar suas movimentações financeiras.
    </div>
</div>

<div style="margin-top:18px;">
    <span class="status">● Interface pronta para conectar ao n8n</span>
</div>

<div class="hero">
    <div class="hero-label">Finan.IA | Assistente pessoal</div>
    <div class="hero-title">Organize seu dinheiro com mais clareza.</div>
    <div class="hero-text">
        Escreva como você falaria normalmente. Por exemplo:
        “Gastei 50 reais no almoço hoje” ou
        “Recebi 300 reais de um serviço”.
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# CARTÕES INFORMATIVOS
# =========================================================

st.markdown(
    '<div class="section-title">Comece por aqui</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">01 / DESPESAS</div>
        <div class="metric-value">Registre seus gastos</div>
        <div class="metric-note">
            Informe quanto gastou e com o que foi a despesa.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">02 / RECEITAS</div>
        <div class="metric-value">Registre suas entradas</div>
        <div class="metric-note">
            Anote os valores recebidos e a origem do dinheiro.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">03 / CONSULTAS</div>
        <div class="metric-value">Converse com a IA</div>
        <div class="metric-note">
            Pergunte sobre as movimentações financeiras registradas.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ÁREA DE CONVERSA
# =========================================================

st.markdown("""
<div class="chat-panel">
    <div class="chat-title">💬 Conversa com o Finan.IA</div>
    <div class="chat-subtitle">
        Digite sua mensagem no campo abaixo
    </div>
</div>
""", unsafe_allow_html=True)

# Exibe o histórico uma única vez.
for mensagem in st.session_state.mensagens:
    papel = mensagem.get("role", "assistant")
    conteudo = mensagem.get("content", "")

    if papel not in ("user", "assistant"):
        papel = "assistant"

    avatar = "user" if papel == "user" else "assistant"

    with st.chat_message(papel, avatar=avatar):
        st.markdown(conteudo)


# =========================================================
# ENVIO DA MENSAGEM PARA O N8N
# =========================================================

pergunta = st.chat_input("Escreva sua mensagem para o Finan.IA...")

if pergunta:
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta,
    })

    with st.chat_message("user", avatar="user"):
        st.markdown(pergunta)

    with st.chat_message("assistant", avatar="assistant"):
        with st.spinner("O Finan.IA está preparando uma resposta..."):
            try:
                resposta = consultar_n8n(pergunta)

            except requests.exceptions.Timeout:
                resposta = (
                    "A solicitação demorou mais do que o esperado. "
                    "Tente novamente e confira se o workflow do n8n "
                    "está ativo."
                )

            except requests.exceptions.HTTPError as erro:
                status = (
                    erro.response.status_code
                    if erro.response is not None
                    else "desconhecido"
                )
                resposta = (
                    f"O webhook retornou um erro HTTP ({status}). "
                    "Confira se o workflow está ativo e se a URL "
                    "do webhook está correta."
                )

            except requests.exceptions.RequestException as erro:
                resposta = (
                    "Não consegui me conectar ao n8n. "
                    "Confira sua conexão e o webhook configurado.\n\n"
                    f"Detalhe técnico: {erro}"
                )

            except Exception as erro:
                resposta = (
                    "Ocorreu um erro ao processar a resposta.\n\n"
                    f"Detalhe técnico: {erro}"
                )

        st.markdown(resposta)

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta,
    })


# =========================================================
# RODAPÉ
# =========================================================

st.markdown("""
<div class="footer">
    Finan.IA — Assistente de organização financeira<br>
    As consultas e movimentações dependem da configuração
    correta do workflow e dos dados no n8n.
</div>
""", unsafe_allow_html=True)
