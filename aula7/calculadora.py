import math
from flask import render_template, request

def calcular():
    if request.method == "GET":
        return render_template("calculadora.html", etapas="", resultados="")

    try:
        num1 = float(request.form["num1"])
    except (ValueError, KeyError):
        return render_template(
            "calculadora.html",
            etapas="Erro: O primeiro número é inválido ou obrigatório.",
            resultados="",
        )

    operacao = request.form.get("operacao")

    if operacao == "sqrt":
        if num1 < 0:
            return render_template(
                "calculadora.html",
                etapas=f"Não existe raiz real de {num1}.",
                resultados="Erro: número negativo",
            )
        resultado = math.sqrt(num1)
        return render_template(
            "calculadora.html",
            etapas=f"√{num1} = {resultado}",
            resultados=str(resultado),
        )

    if operacao == "log":
        if num1 <= 0:
            return render_template(
                "calculadora.html",
                etapas=f"O logaritmo não está definido para {num1}.",
                resultados="Erro: número menor ou igual a zero",
            )
        resultado = math.log10(num1)
        return render_template(
            "calculadora.html",
            etapas=f"log10({num1}) = {resultado}",
            resultados=str(resultado),
        )

    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados="",
        )

    try:
        num2 = float(num2_valor)
    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Erro: O segundo número fornecido é inválido.",
            resultados="",
        )

    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"
    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"
    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} × {num2} = {resultado}"
    elif operacao == "/":
        if num2 == 0:
            return render_template(
                "calculadora.html",
                etapas=f"{num1} ÷ {num2}",
                resultados="Erro: Divisão por zero",
            )
        resultado = num1 / num2
        etapas = f"{num1} ÷ {num2} = {resultado}"
    elif operacao == "**":
        resultado = math.pow(num1, num2)
        etapas = f"{num1} ^ {num2} = {resultado}"
    else:
        return render_template(
            "calculadora.html",
            etapas="Operação inválida selecionada.",
            resultados="",
        )

    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=str(resultado),
    )
