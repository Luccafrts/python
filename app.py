from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def questao1():
    return render_template("questao1.html", name ="pedro da silva me mimei camilo brum souza pinto cum nery alvez alvares cornelio anthony ansur gomide pereira braulio coelho do gordo paiva cachorro macaco marco cobra duarte braga oliveira perceval seleme proti susu andradas antonio carlos vargas muniz elias leite ")

@app.route("/questao2")
def questao2():
    dados = [{"nome": "lucca", "idade":17}]

    return render_template("questao2.html", alunos=dados)
    



if __name__ == "__main__":
    app.run(debug=True)