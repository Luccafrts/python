from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return'''

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Currículo Profissional</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <style>
        :root {
            --primary-color: #2c3e50;
            --accent-color: #3498db;
            --text-dark: #333;
            --text-light: #7f8c8d;
            --bg-body: #f4f7f6;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background-color: var(--bg-body);
            color: var(--text-dark);
            line-height: 1.6;
            display: flex;
            justify-content: center;
            padding: 40px 20px;
        }

        .cv-container {
            background: #fff;
            width: 100%;
            max-width: 900px;
            display: grid;
            grid-template-columns: 300px 1fr;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }

        /* Coluna Lateral */
        .sidebar {
            background-color: var(--primary-color);
            color: #fff;
            padding: 40px 30px;
        }

        .profile-img {
            width: 150px;
            height: 150px;
            background: #ddd;
            border-radius: 0%;
            margin: 0 auto 20px;
            display: block;
            border: 4px solid var(--accent-color);
        }

        .sidebar h2 { font-size: 1.2rem; margin-bottom: 20px; border-bottom: 1px solid #555; padding-bottom: 5px; }
        .contact-item { margin-bottom: 15px; font-size: 0.8rem; }
        .contact-item i { margin-right: 10px; color: var(--accent-color); }

        .skills-list { list-style: none; }
        .skills-list li { margin-bottom: 8px; font-size: 0.9rem; background: rgba(255,255,255,0.1); padding: 5px 10px; border-radius: 4px; }

        /* Coluna Principal */
        .main-content { padding: 50px; }
        
        .header-main h1 { font-size: 2.5rem; color: var(--primary-color); text-transform: uppercase; margin-bottom: 5px; }
        .header-main p { font-size: 1.1rem; color: var(--accent-color); font-weight: bold; margin-bottom: 30px; }

        .section { margin-bottom: 35px; }
        .section-title { font-size: 1.4rem; color: var(--primary-color); text-transform: uppercase; margin-bottom: 15px; border-left: 5px solid var(--accent-color); padding-left: 15px; }

        .job { margin-bottom: 20px; }
        .job-header { display: flex; justify-content: space-between; font-weight: bold; }
        .job-company { color: var(--accent-color); }
        .job-desc { font-size: 0.95rem; color: var(--text-light); margin-top: 5px; }

        /* Responsividade */
        @media (max-width: 768px) {
            .cv-container { grid-template-columns: 1fr; }
            .sidebar { text-align: center; }
        }
    </style>
</head>
<body>

<div class="cv-container">
    <!-- Sidebar -->
    <aside class="sidebar">
        <div class="profile-img"><img src="https://media1.tenor.com/m/wsChytFfrS4AAAAd/monki-flip-monkey.gif" alt="Meu gif" width="143" height="140">
</div> 
        
        <h2>CONTATO</h2>
        <div class="contact-item"><i class="fas fa-phone"></i> (31) 67676-7676</div>
        <div class="contact-item"><i class="fas fa-envelope"></i> luccabrumdasilvamemimeni@resenha.com</div>
        <div class="contact-item"><i class="fas fa-map-marker-alt"></i> Sua Cidade, Estado</div>
        <div class="contact-item"><i class="fab fa-linkedin"></i> ://linkedin.com</div>
        <div class="contact-item"><i class="fab fa-github"></i> ://github.com</div>

        <h2 style="margin-top: 40px;">HABILIDADES</h2>
        <ul class="skills-list">
            <li>Python & Flask</li>
            <li>Desenvolvimento Web (HTML/CSS)</li>
            <li>SQL & Bancos de Dados</li>
            <li>Git & Versionamento</li>
            <li>APIs RESTful</li>
        </ul>
    </aside>

    <!-- Conteúdo Principal -->
    <main class="main-content">
        <header class="header-main">
            <h1> Lucca Brum da Silva me mimeni Camilo Cobra Quelotti Anthony paiva amorin gonçalves pinto</h1>
            <p>Desenvolvedor Backend Python / Flask</p>
        </header>

        <section class="section">
            <h2 class="section-title">Resumo</h2>
            <p>Profissional dedicado com foco em desenvolvimento de sistemas web. Experiência técnica em Python, criação de rotas dinâmicas, uso de decorators e integração com APIs. Busco aplicar soluções eficientes e código limpo.</p>
        </section>

        <section class="section">
            <h2 class="section-title">Experiência Profissional</h2>
            
            <div class="job">
                <div class="job-header">
                    <span>Desenvolvedor de Software</span>
                    <span>2022 - Atual</span>
                </div>
                <div class="job-company">Nome da Empresa Exemplo</div>
                <p class="job-desc">Desenvolvimento de funcionalidades backend, manutenção de servidores Flask e otimização de consultas SQL.</p>
            </div>

            <div class="job">
                <div class="job-header">
                    <span>Estagiário em TI</span>
                    <span>2021 - 2022</span>
                </div>
                <div class="job-company">Outra Empresa S.A.</div>
                <p class="job-desc">Suporte ao time de desenvolvimento e automação de tarefas repetitivas usando scripts Python.</p>
            </div>
        </section>

        <section class="section">
            <h2 class="section-title">Formação Acadêmica</h2>
            <div class="job">
                <div class="job-header">
                    <span>Sistemas de Informação (ou seu curso)</span>
                    <span>Conclusão 2024</span>
                </div>
                <div class="job-company">Universidade Exemplo</div>
            </div>
        </section>
    </main>
</div>

</body>
</html>


'''


if __name__ == '__main__':
    app.run(debug=True)
