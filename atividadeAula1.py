'''Crie uma aplicação Flask que contenha uma rota específica responsável por explicar o conceito de decorator em Python.
Requisitos
Crie uma rota acessível por meio do caminho: /decorator
Ao acessar essa rota no navegador, deve ser exibido um texto explicando:
O que é um decorator em Python
Para que ele serve
Como ele é utilizado no Flask (exemplo: @app.route)'''

from flask import Flask

app = Flask(__name__)
@app.route('/')
def decorator():
    return'''
    <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Entendendo Decorators em Python</title>
    <style>
        :root {
            --primary: #3776ab;
            --secondary: #ffd343;
            --dark: #2c3e50;
            --light: #f8f9fa;
            --code-bg: #1e1e1e;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--dark);
            background-color: var(--light);
            margin: 0;
            padding: 0;
        }

        header {
            background-color: var(--primary);
            color: white;
            padding: 2rem 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        main {
            max-width: 900px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .card {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 15px rgba(0,0,0,0.05);
        }

        h2 {
            color: var(--primary);
            border-bottom: 2px solid var(--secondary);
            display: inline-block;
            margin-top: 0;
        }

        code {
            background-color: var(--code-bg);
            color: #dcdcdc;
            padding: 0.2rem 0.4rem;
            border-radius: 4px;
            font-family: 'Courier New', Courier, monospace;
        }

        pre {
            background-color: var(--code-bg);
            color: #dcdcdc;
            padding: 1.5rem;
            border-radius: 8px;
            overflow-x: auto;
            border-left: 5px solid var(--secondary);
        }

        .highlight { color: #569cd6; } /* Azul */
        .string { color: #ce9178; }    /* Laranja */
        .comment { color: #6a9955; }   /* Verde */
        .decorator { color: #dcdcaa; } /* Amarelo */

        .flask-box {
            background-color: #e3f2fd;
            border-left: 5px solid var(--primary);
            padding: 1rem;
            margin-top: 1rem;
        }
    </style>
</head>
<body>

<header>
    <h1>Guia Visual: Decorators em Python</h1>
    <p>A "mágica" por trás do <code>@</code> no seu código</p>
</header>

<main>
    <section class="card">
        <h2>O que é um Decorator?</h2>
        <p>Um <strong>Decorator</strong> é essencialmente uma função que recebe outra função como argumento e retorna uma nova função com um comportamento "embrulhado" (estendido).</p>
        <p>Imagine que a função original é um presente, e o decorator é o papel de embrulho e o laço que você coloca por fora sem mexer no que está dentro.</p>
    </section>

    <section class="card">
        <h2>Para que serve?</h2>
        <ul>
            <li><strong>Reaproveitamento:</strong> Evita repetir o mesmo código em várias funções.</li>
            <li><strong>Organização:</strong> Separa a lógica principal (ex: processar um pedido) de lógicas secundárias (ex: verificar se o usuário tem permissão).</li>
            <li><strong>Monitoramento:</strong> Ótimo para criar logs ou medir o tempo de execução automaticamente.</li>
        </ul>
    </section>

    <section class="card">
        <h2>O Caso do Flask: <code>@app.route</code></h2>
        <p>No Flask, o decorator é usado para fazer o <strong>roteamento</strong>. Ele "avisa" ao servidor que uma função específica deve responder a um endereço da web.</p>
        
        <div class="flask-box">
            <strong>Como o Flask interpreta isso:</strong><br>
            "Ei Flask, toda vez que alguém acessar a URL <code>/contato</code>, execute a função <code>exibir_contato()</code> logo abaixo."
        </div>

        <pre>
<span class="highlight">from</span> flask <span class="highlight">import</span> Flask
app = Flask(__name__)

<span class="decorator">@app.route</span>(<span class="string">'/home'</span>)
<span class="highlight">def</span> <span class="decorator">index</span>():
    <span class="highlight">return</span> <span class="string">"Bem-vindo à Home!"</span>

<span class="comment"># Sem o decorator, o Flask não saberia 
# qual URL deve ativar esta função.</span></pre>
    </section>

    <section class="card">
        <h2>Exemplo de Estrutura Interna</h2>
        <p>Veja como um decorator simples funciona "por baixo do capô":</p>
        <pre>
<span class="highlight">def</span> <span class="decorator">meu_decorador</span>(funcao_original):
    <span class="highlight">def</span> <span class="decorator">wrapper</span>():
        print(<span class="string">"Executando ANTES da função..."</span>)
        funcao_original()
        print(<span class="string">"Executando DEPOIS da função..."</span>)
    <span class="highlight">return</span> wrapper

<span class="decorator">@meu_decorador</span>
<span class="highlight">def</span> <span class="decorator">dizer_oi</span>():
    print(<span class="string">"Oi!"</span>)</pre>
    </section>
</main>

</body>
</html>

'''

if __name__ == '__main__':
    app.run(debug=True)