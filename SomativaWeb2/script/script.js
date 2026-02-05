// Animação Foto

const foto = document.querySelector('.foto-empresa');
window.addEventListener('DOMContentLoaded', () => {
    foto?.classList.add('aparecer');
});

// Tudo dentro do mesmo DOMContentLoaded

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const telefoneInput = document.getElementById("telefone_usuario");

    // Máscara automatica do telefone 

    telefoneInput.addEventListener("input", (e) => {
        let valor = e.target.value.replace(/\D/g, ""); 

        if (valor.length > 11) valor = valor.slice(0, 11); 

        if (valor.length > 6) {
            e.target.value = `(${valor.slice(0, 2)}) ${valor.slice(2, 7)}-${valor.slice(7)}`;
        } else if (valor.length > 2) {
            e.target.value = `(${valor.slice(0, 2)}) ${valor.slice(2)}`;
        } else {
            e.target.value = valor;
        }
    });

    // Verificação do formulário 
    
    form.addEventListener("submit", (event) => {
        const nome = document.getElementById("nome_usuario").value.trim();
        const email = document.getElementById("gmail_usuario").value.trim();
        const telefone = telefoneInput.value.trim();
        const termos = document.getElementById("temos_servico").checked;

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const telefoneRegex = /^\(\d{2}\)\s\d{4,5}-\d{4}$/;

        if (nome === "") {
            alert("Por favor, preencha seu nome.");
            event.preventDefault();
            return;
        }

        if (!emailRegex.test(email)) {
            alert("Digite um Gmail válido.");
            event.preventDefault();
            return;
        }

        if (!telefoneRegex.test(telefone)) {
            alert("Digite um telefone válido no formato (xx) xxxxx-xxxx.");
            event.preventDefault();
            return;
        }

        if (!termos) {
            alert("Você precisa concordar com os termos de serviço.");
            event.preventDefault();
            return;
        }

        alert("Formulário enviado com sucesso!");
    });
});
