# 💰 Finan.IA — Assistente Financeiro Inteligente

**Assistente financeiro conversacional desenvolvido com Python, Streamlit, n8n e Inteligência Artificial.**

O Finan.IA é um projeto acadêmico que busca facilitar o controle financeiro pessoal por meio de uma interface de chat. O usuário pode escrever solicitações em linguagem natural para registrar receitas e despesas, consultar seu saldo e obter extratos financeiros.

O projeto integra uma interface desenvolvida em Python a um fluxo de automação no n8n, utilizando um agente de Inteligência Artificial com Google Gemini para interpretar as mensagens e auxiliar na execução das operações.

---

## 📌 Sobre o projeto

O controle financeiro pessoal é importante para acompanhar receitas, despesas e saldo disponível. Entretanto, manter registros manualmente pode exigir tempo e organização.

O Finan.IA propõe uma alternativa conversacional, permitindo que o usuário interaja com o sistema por meio de mensagens simples, como:

- “Recebi R$ 1.500,00 de salário.”
- “Gastei R$ 35,00 com alimentação hoje.”
- “Qual é o meu saldo atual?”
- “Mostre meu extrato mensal.”

A aplicação foi desenvolvida com finalidade acadêmica e demonstra a integração entre desenvolvimento Python, interfaces web, automação de processos e Inteligência Artificial.

## 🎯 Objetivos

- Desenvolver uma interface de chat intuitiva e visualmente personalizada.
- Facilitar o registro de receitas e despesas em linguagem natural.
- Integrar a interface Python a um webhook do n8n.
- Utilizar Inteligência Artificial para interpretar as solicitações do usuário.
- Armazenar e consultar movimentações financeiras em uma tabela de dados.
- Apresentar informações como saldo e extrato mensal com base nos registros disponíveis.
- Aplicar conceitos de programação, integração de sistemas e automação.

## ✨ Funcionalidades

- **Interface conversacional:** interação por mensagens.
- **Registro financeiro:** suporte ao registro de receitas e despesas.
- **Consulta de saldo:** cálculo de receitas menos despesas registradas.
- **Extrato mensal:** consulta das movimentações por período.
- **Interpretação de linguagem natural:** utilização de um agente de IA.
- **Integração com automação:** comunicação entre Python e n8n por HTTP.
- **Tratamento de erros:** tratamento de falhas de comunicação e respostas inesperadas.
- **Memória de conversa:** utilização do recurso Simple Memory no fluxo configurado.

> A execução de cada funcionalidade depende da configuração correta do fluxo no n8n, das ferramentas conectadas e dos dados disponíveis na tabela.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem utilizada no desenvolvimento da aplicação. |
| Streamlit | Criação da interface web interativa. |
| Requests | Comunicação HTTP entre a aplicação e o webhook. |
| n8n | Automação e integração entre os componentes. |
| Google Gemini | Modelo de IA utilizado pelo agente para interpretar mensagens. |
| Simple Memory | Apoio à continuidade contextual da conversa. |
| Data Table do n8n | Armazenamento e consulta das movimentações financeiras. |
| JSON | Formato utilizado na comunicação entre os sistemas. |
| GitHub | Versionamento e disponibilização do código-fonte. |

## 🏗️ Arquitetura do sistema

O funcionamento geral do Finan.IA pode ser representado pelo fluxo abaixo:

```text
┌─────────────────────────────┐
│          USUÁRIO            │
│   Envia mensagem no chat    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      PYTHON + STREAMLIT     │
│     Interface conversacional│
└──────────────┬──────────────┘
               │ HTTP POST / JSON
               ▼
┌─────────────────────────────┐
│        WEBHOOK n8n          │
│     Recebe a solicitação    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      AGENTE DE IA           │
│    Google Gemini            │
│ Interpreta a mensagem       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     FERRAMENTAS E DADOS     │
│     Data Table do n8n       │
│ Registro e consultas        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   RESPOND TO WEBHOOK        │
│    Retorna a resposta       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       CHAT FINAN.IA         │
│ Exibe o resultado ao usuário│
└─────────────────────────────┘
```

### Etapas do funcionamento

1. O usuário digita uma mensagem na interface Streamlit.
2. A aplicação Python envia a mensagem em formato JSON para o webhook.
3. O n8n recebe a solicitação e encaminha a mensagem ao agente de IA.
4. O agente interpreta a intenção e utiliza as ferramentas disponíveis, quando necessário.
5. As movimentações são armazenadas ou consultadas na tabela de dados.
6. O nó Respond to Webhook retorna o resultado.
7. A aplicação apresenta a resposta no chat.

## 🗃️ Estrutura dos dados financeiros

A tabela utilizada no fluxo é identificada como `movimentacoes_finania`.

Os campos principais são:

| Campo | Descrição |
|---|---|
| `usuario_id` | Identificador do usuário associado ao lançamento. |
| `data` | Data da movimentação. |
| `tipo` | Tipo da movimentação: receita ou despesa. |
| `categoria` | Categoria financeira. |
| `descricao` | Descrição do lançamento. |
| `valor_centavos` | Valor monetário armazenado em centavos inteiros. |

**Exemplo:** uma movimentação de R$ 25,00 corresponde a `2500` centavos.

O saldo é calculado pela diferença entre o total das receitas e o total das despesas registradas.

## 💻 Como executar o projeto

### 1. Pré-requisitos

Antes de iniciar, é necessário ter:

- Python instalado;
- Acesso ao repositório do projeto;
- Bibliotecas Python utilizadas pela aplicação;
- Um fluxo n8n configurado e ativo;
- Acesso aos serviços e às credenciais necessários para o agente de IA.

### 2. Clonar o repositório

Com o Git instalado, execute:

```bash
git clone https://github.com/mickaelsousamiranda-lgtm/Finan-IA.git
cd Finan-IA
```

Se não tiver o Git instalado, você também pode abrir o repositório no GitHub e selecionar **Code → Download ZIP**. Depois, extraia os arquivos em uma pasta.

### 3. Criar um ambiente virtual (opcional, recomendado)

No Windows:

```powershell
python -m venv .venv
```

Ative o ambiente:

```powershell
.venv\Scripts\Activate.ps1
```

Se o terminal utilizado for o Prompt de Comando (CMD), use:

```cmd
.venv\Scripts\activate.bat
```

### 4. Instalar as dependências

Instale as bibliotecas utilizadas pela aplicação:

```bash
python -m pip install streamlit requests
```

### 5. Executar a aplicação

No terminal, dentro da pasta do projeto, execute:

```bash
python -m streamlit run finania.py
```

O Streamlit normalmente abrirá a aplicação no navegador. Caso isso não aconteça, utilize o endereço local exibido no terminal.

### 6. Configurar o n8n

O fluxo precisa estar configurado para receber as mensagens e devolver uma resposta ao webhook.

A estrutura principal utilizada no projeto é:

```text
Webhook → AI Agent → Respond to Webhook
```

O fluxo também utiliza o modelo Google Gemini, o recurso Simple Memory e ferramentas de acesso à tabela de dados.

No nó Webhook, a requisição deve receber o campo `chatInput`. No agente de IA, o campo **Prompt (User Message)** deve apontar para a mensagem recebida pelo webhook.

A aplicação Python precisa utilizar a URL correta do webhook configurado no n8n.

## 🧪 Testes sugeridos

Para verificar o funcionamento do sistema, recomenda-se executar os seguintes testes com dados fictícios:

| Teste | Solicitação | Resultado esperado |
|---|---|---|
| Registro de despesa | “Gastei R$ 12,00 com café hoje.” | A movimentação deve ser registrada e confirmada após a gravação. |
| Consulta de saldo | “Qual é meu saldo atual?” | O sistema deve consultar os registros e calcular o saldo. |
| Extrato mensal | “Mostre meu extrato de outubro de 2026.” | O sistema deve consultar as movimentações do período solicitado. |
| Dados incompletos | “Registre uma despesa.” | O agente deve solicitar os dados obrigatórios que faltam. |
| Falha de comunicação | Enviar uma mensagem com o webhook indisponível. | A aplicação deve informar que não conseguiu obter uma resposta. |

Esses cenários são recomendações de validação. O resultado de cada teste deve ser confirmado na aplicação e no fluxo do n8n.

## 🔐 Segurança e limitações

O Finan.IA é um protótipo acadêmico e não deve ser utilizado como sistema bancário ou contábil de produção.

Alguns pontos importantes:

- A URL do webhook configurada no código pode ser acionada por terceiros se estiver pública.
- Credenciais, senhas e chaves privadas não devem ser publicadas no GitHub.
- A configuração atual utiliza um identificador de usuário fixo para a demonstração.
- Consultas e gravações devem ser verificadas antes de apresentar resultados ao usuário.
- Respostas geradas por IA podem conter interpretações incorretas; valores e movimentações devem ser validados com os dados armazenados.
- A disponibilidade depende da aplicação, do webhook, do n8n e dos serviços externos utilizados.

## 🚀 Melhorias futuras

Entre as melhorias planejadas para versões futuras, destacam-se:

- Autenticação e identificação individual dos usuários;
- Validação mais rigorosa de datas e valores;
- Prevenção de lançamentos duplicados;
- Edição e exclusão controlada de movimentações;
- Padronização do formato das respostas do webhook;
- Testes automatizados;
- Melhorias no tratamento de erros e no registro de eventos;
- Relatórios e gráficos financeiros;
- Aprimoramento da segurança e da configuração de segredos.

## 👥 Integrantes

- **Mickael de Sousa Miranda**
- **Pedro Igor**

**Instituição:** Centro Universitário de Balsas — UNIBALSAS  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Projeto:** Finan.IA — Assistente Financeiro Inteligente

## 📂 Repositório

Código-fonte disponível em:

🔗 [https://github.com/mickaelsousamiranda-lgtm/Finan-IA](https://github.com/mickaelsousamiranda-lgtm/Finan-IA)

## 📄 Considerações finais

O Finan.IA demonstra a aplicação prática de Python, interfaces web, automação de processos e Inteligência Artificial na construção de um assistente financeiro conversacional.

O desenvolvimento permitiu explorar a comunicação entre sistemas por meio de webhooks, a interpretação de mensagens em linguagem natural e o uso de dados estruturados para apoiar consultas financeiras.

O projeto constitui uma base acadêmica para estudos e futuras melhorias relacionadas à usabilidade, confiabilidade, segurança e expansão de funcionalidades.

---

*Projeto desenvolvido para fins acadêmicos e educacionais.*
