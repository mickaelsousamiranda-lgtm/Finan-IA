# Finan.IA — Assistente Financeiro Inteligente

## 1. Sobre o projeto

O **Finan.IA** é um assistente financeiro inteligente desenvolvido para auxiliar os usuários na organização e no controle de suas movimentações financeiras por meio de uma interface conversacional.

O sistema utiliza Python e Streamlit para a interface, enquanto o n8n realiza a integração entre o webhook, o agente de inteligência artificial e os recursos de armazenamento de dados. O modelo Google Gemini é utilizado para interpretar as mensagens e gerar respostas ao usuário.

O projeto foi desenvolvido com finalidade acadêmica, permitindo explorar a integração entre desenvolvimento web, automação de processos, inteligência artificial e gerenciamento de dados.

## 2. Objetivos

- Desenvolver uma interface conversacional para interação com um assistente financeiro.
- Integrar uma aplicação Python a um fluxo de automação criado no n8n.
- Utilizar inteligência artificial para interpretar solicitações em linguagem natural.
- Estruturar dados de movimentações financeiras.
- Demonstrar a comunicação entre diferentes tecnologias por meio de requisições HTTP e dados em formato JSON.

## 3. Funcionalidades

- Interface de chat desenvolvida com Streamlit.
- Envio de mensagens do usuário para o assistente financeiro.
- Integração com um webhook do n8n.
- Processamento de mensagens por um agente de inteligência artificial.
- Utilização do Google Gemini para geração de respostas.
- Uso de memória conversacional para manter o contexto da interação, conforme a configuração do fluxo.
- Integração com uma tabela de dados para estruturar movimentações financeiras.
- Tratamento de erros de comunicação e tempo limite de requisições.

## 4. Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Linguagem utilizada no desenvolvimento da aplicação. |
| Streamlit | Construção da interface gráfica e do chat. |
| Requests | Comunicação HTTP entre a aplicação Python e o webhook. |
| n8n | Orquestração do fluxo de automação. |
| Google Gemini | Interpretação das mensagens e geração de respostas pelo agente de IA. |
| Simple Memory | Apoio à manutenção do contexto conversacional. |
| n8n Data Table | Estruturação e armazenamento de dados financeiros, conforme o fluxo configurado. |
| JSON | Formato utilizado na troca de informações entre os componentes. |
| GitHub | Versionamento e disponibilização do código-fonte. |

## 5. Arquitetura do sistema

O funcionamento do Finan.IA ocorre por meio da integração entre a interface desenvolvida em Python e o fluxo de automação configurado no n8n.

```text
Usuário
   |
   v
Interface Python + Streamlit
   |
   v
Requisição HTTP com dados em JSON
   |
   v
Webhook do n8n
   |
   v
Agente de Inteligência Artificial
   |
   v
Google Gemini
   |
   v
Memória conversacional e recursos de dados
   |
   v
Resposta do n8n
   |
   v
Exibição da resposta no chat
```

A aplicação envia a mensagem do usuário ao webhook. O n8n recebe os dados e encaminha o conteúdo ao agente de inteligência artificial. Após o processamento, a resposta é retornada à aplicação para exibição na interface.

## 6. Estrutura dos dados financeiros

O fluxo foi estruturado para trabalhar com os seguintes campos de movimentação financeira:

| Campo | Descrição |
|---|---|
| `usuario_id` | Identificador do usuário. |
| `data` | Data da movimentação financeira. |
| `tipo` | Tipo da movimentação, como entrada ou saída. |
| `categoria` | Categoria financeira da movimentação. |
| `descricao` | Descrição da movimentação. |
| `valor_centavos` | Valor monetário armazenado em centavos. |

**Exemplo de representação monetária:**

Um valor de R$ 25,00 corresponde a `2500` centavos.

O uso de centavos como números inteiros ajuda a evitar imprecisões comuns em operações financeiras realizadas com números de ponto flutuante.

## 7. Requisitos para execução

Antes de executar o projeto, é necessário ter instalado:

- Python 3.
- Gerenciador de pacotes pip.
- Acesso ao webhook do n8n configurado para o projeto.
- Dependências Python utilizadas pela aplicação.

## 8. Instalação e execução

### 8.1. Clonar o repositório

```bash
git clone https://github.com/mickaelsousamiranda-lgtm/Finan-IA.git
```

### 8.2. Acessar a pasta do projeto

```bash
cd Finan-IA
```

### 8.3. Instalar as dependências

```bash
python -m pip install streamlit requests
```

### 8.4. Executar a aplicação

```bash
python -m streamlit run finania.py
```

Após iniciar o Streamlit, acesse o endereço local apresentado no terminal para utilizar a interface.

## 9. Configuração da integração com o n8n

Para que a aplicação funcione corretamente, o fluxo do n8n deve estar configurado e acessível.

A estrutura utilizada no projeto contempla os seguintes componentes:

1. **Webhook:** recebe a mensagem enviada pela aplicação Python.
2. **AI Agent:** processa a mensagem recebida.
3. **Google Gemini:** fornece o modelo de linguagem utilizado pelo agente.
4. **Simple Memory:** auxilia na manutenção do contexto da conversa.
5. **Data Table:** permite trabalhar com os dados financeiros estruturados.
6. **Respond to Webhook:** retorna a resposta do fluxo à aplicação.

A mensagem enviada pela aplicação contém os campos `chatInput`, `usuario_id` e `sessionId`.

O agente deve utilizar o campo `chatInput` recebido pelo webhook como mensagem de entrada. A configuração correta desse campo é necessária para evitar que o agente receba uma solicitação vazia.

## 10. Testes e validação

A validação do sistema pode incluir os seguintes cenários:

- Verificar se a interface Streamlit é iniciada corretamente.
- Enviar uma mensagem pelo chat e confirmar o recebimento pelo webhook.
- Verificar se o agente de inteligência artificial recebe a mensagem.
- Confirmar se a resposta do n8n é exibida na interface.
- Avaliar o comportamento em caso de falha de conexão ou tempo limite.
- Verificar a consistência dos dados financeiros registrados na tabela.
- Testar se o contexto conversacional é mantido conforme a configuração da memória.

Esses itens representam cenários de validação. Os resultados devem ser registrados após a execução efetiva de cada teste.

## 11. Limitações e melhorias futuras

O projeto pode ser ampliado com novas funcionalidades, incluindo:

- Cadastro e autenticação de usuários.
- Separação segura dos dados por usuário.
- Registro e consulta de receitas e despesas.
- Geração de relatórios financeiros.
- Painel de indicadores com gráficos e estatísticas.
- Filtros por período e categoria.
- Exportação de relatórios.
- Aprimoramento da validação dos dados.
- Proteção de configurações e credenciais por meio de variáveis de ambiente.

As funcionalidades mencionadas nesta seção são propostas para futuras versões e não devem ser consideradas implementadas sem a respectiva validação.

## 12. Considerações finais

O Finan.IA demonstra a aplicação prática de conceitos de desenvolvimento de software, automação de processos e inteligência artificial. A integração entre Python, Streamlit e n8n permite construir uma interface conversacional conectada a um agente de IA, demonstrando como diferentes tecnologias podem trabalhar em conjunto para apoiar tarefas relacionadas à organização financeira.

O projeto também oferece uma base para estudos e melhorias futuras na área de sistemas inteligentes aplicados à gestão financeira.

## 13. Informações acadêmicas

**Projeto:** Finan.IA — Assistente Financeiro Inteligente  
**Instituição:** UNIBALSAS  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Integrantes:** Mickael de Sousa Miranda e Pedro Igor

## 14. Repositório

Código-fonte disponível no GitHub:

https://github.com/mickaelsousamiranda-lgtm/Finan-IA
