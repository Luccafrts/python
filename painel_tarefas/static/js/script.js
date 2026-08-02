// Alternância de modo escuro/claro, com preferência salva no localStorage
(function () {
    const CHAVE_LOCALSTORAGE = "modoEscuro";
    const botao = document.getElementById("btnModoEscuro");
    const corpo = document.body;

    function aplicarModo(ativo) {
        if (ativo) {
            corpo.classList.add("bg-dark", "text-light");
            if (botao) botao.innerHTML = '<i class="bi bi-sun"></i>';
        } else {
            corpo.classList.remove("bg-dark", "text-light");
            if (botao) botao.innerHTML = '<i class="bi bi-moon-stars"></i>';
        }
    }

    // Carrega preferência salva ao abrir a página
    const preferenciaSalva = localStorage.getItem(CHAVE_LOCALSTORAGE) === "true";
    aplicarModo(preferenciaSalva);

    if (botao) {
        botao.addEventListener("click", function () {
            const modoAtivo = !corpo.classList.contains("bg-dark");
            aplicarModo(modoAtivo);
            localStorage.setItem(CHAVE_LOCALSTORAGE, modoAtivo);
        });
    }
})();
