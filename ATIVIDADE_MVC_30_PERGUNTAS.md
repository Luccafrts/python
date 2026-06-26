# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Lucca Freitas
- Turma: 3c2

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

As classes que representam as tabelas ficam na pasta models/.

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

O banco é streamflix.db e a configuração está em app.py.

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

ModeloBase (base.py), FilmeFavorito (filme_favorito.py) e HistoricoBusca (historico_busca.py).

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

Herdam de ModeloBase e recebem id, data_criacao e data_atualizacao.

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

__tablename__ = filmes_favoritos; define o nome da tabela no banco.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

tmdb_id; possui unique=True e nullable=False.


**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

O método verifica duplicidade, cria o favorito, salva no banco e retorna o objeto; se já existir, não adiciona.

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

Classe HistoricoBusca, método ultimas().

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

Salva apenas alguns campos, como tmdb_id, titulo, poster_path e nota (além do ano).

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?


Exporta ModeloBase, FilmeFavorito e HistoricoBusca além de db, facilitando as importações.

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

Existem três Blueprints: dashboard, filmes (/filmes) e favoritos (/favoritos).

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

controllers/filmes_controller.py, função populares().

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

Busca filmes populares pela API e consulta a lista de favoritos antes do render_template.

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

O controller filmes_controller registra usando o model HistoricoBusca.

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

POST; exemplo: /favoritos/adicionar/550.

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

Redireciona para /filmes/populares.

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

Em app.py com app.register_blueprint(...).

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

dashboard_controller.py; envia populares, melhores, total_favoritos, historico e modo_demo.

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

É a camada Service; é chamada pelos controllers para acessar a API TMDB.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

O termo vem de request.args porque o formulário usa GET.

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

views/templates/.

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

layout.html; os demais usam {% extends 'layout.html' %}.


**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

StreamFlix, Populares, Melhores, Buscar e Favoritos com url_for correspondente.

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

views/templates/filmes/detalhe.html; a variável vem de api.streaming().

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

É um template parcial reutilizado com {% include 'filmes/_card.html' %}.

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

A variável favorito controla Salvar/Remover.

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

views/static/css/style.css; carregado com url_for('static', filename='css/style.css').

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

{% for fav in favoritos %}; mostra título, nota e ano.

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

Mostra aviso de modo demonstração; a variável é fornecida por um context_processor em app.py.

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

View detalhe.html → favoritos_controller.py → FilmeFavorito.adicionar() → grava no banco → redirect para o detalhe.
---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
