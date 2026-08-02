# Painel de Controle de Tarefas (Flask)

Projeto desenvolvido para a atividade prática de Flask, com gerenciamento de
rotas e templates, banco SQLite, autenticação de usuários, CRUD completo de
tarefas, integração com API externa e interface em Bootstrap 5.

## Como executar

1. (Opcional, mas recomendado) crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. (Opcional) defina variáveis de ambiente antes de rodar:
   ```bash
   export SECRET_KEY="troque-por-uma-chave-segura"
   export FLASK_DEBUG=1     # apenas em desenvolvimento; em produção deixe 0/omita
   ```

4. Rode a aplicação:
   ```bash
   python app.py
   ```

5. Acesse **http://127.0.0.1:5000** no navegador. Crie uma conta em
   "Criar conta" e faça login para usar o painel.

## Estrutura

```
painel_tarefas/
├── app.py                 # rotas, autenticação, CRUD, integração com API
├── database.db             # criado automaticamente na primeira execução
├── requirements.txt
├── static/
│   ├── css/style.css       # estilos + modo escuro
│   └── js/script.js        # alternância de modo escuro (localStorage)
└── templates/
    ├── base.html            # layout base, menu, navbar
    ├── login.html
    ├── registro.html
    ├── dashboard.html        # lista de tarefas + filtro por status + frase do dia
    ├── form_tarefa.html      # criação/edição de tarefas
    └── progresso.html        # gráficos de progresso (Chart.js)
```

## Recursos implementados

- **Rotas**: `/`, `/login`, `/registro`, `/logout`, `/dashboard`,
  `/nova_tarefa`, `/editar/<id>`, `/excluir/<id>`, `/concluir/<id>`,
  `/dashboard/progresso`, além das rotas JSON `/api/tarefas` e
  `/api/progresso`.
- **Banco de dados SQLite**: tabelas `usuarios` (id, nome, email, senha) e
  `tarefas` (id, titulo, descricao, status, usuario_id).
- **Autenticação**: senha protegida com hash (`werkzeug.security`), sessão
  do Flask e decorator `@login_requerido` protegendo rotas internas.
- **CRUD completo de tarefas**, com status Pendente/Em andamento/Concluída
  (amarelo, azul, verde) e botão de conclusão rápida.
- **Integração com API externa**: frase motivacional diária via
  `https://api.adviceslip.com/advice`, exibida no `/dashboard`.
- **Interface**: Bootstrap 5 + Bootstrap Icons, layout responsivo, cards de
  tarefas, dropdown de filtro por status.
- **Modo escuro**: alternado por botão na navbar, preferência persistida em
  `localStorage`.
- **Dashboard de progresso**: gráficos de barras e pizza (Chart.js),
  alimentados pela rota `/api/progresso` (JSON).
- **Segurança/boas práticas**: `SECRET_KEY` lida de variável de ambiente,
  `DEBUG=False` por padrão (controlado por `FLASK_DEBUG`).

## Próximos passos sugeridos (desafios do exercício)

- Persistir a preferência do modo escuro por usuário (hoje é por navegador).
- Adicionar paginação/gráficos adicionais ao dashboard de progresso.
