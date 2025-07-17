// script.js

async function sendCalculation() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;
    const outputResult = document.getElementById('outputResult');

    // Validar se os números são válidos ANTES de enviar para o backend
    if (isNaN(num1) || isNaN(num2)) {
        outputResult.textContent = "Por favor, insira números válidos.";
        outputResult.style.color = "red";
        return;
    }

    try {
        // Envia os dados para a rota /calculate do seu backend Flask
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ // Converte o objeto JavaScript em uma string JSON
                num1: num1,
                num2: num2,
                operation: operation
            })
        });

        // Verifica se a resposta foi bem-sucedida (status 2xx)
        if (response.ok) {
            const data = await response.json(); // Pega a resposta JSON do backend
            outputResult.textContent = data.result;
            outputResult.style.color = "#007bff";
        } else {
            // Se houver um erro do servidor (ex: 400 Bad Request)
            const errorData = await response.json();
            outputResult.textContent = errorData.error || "Ocorreu um erro no servidor.";
            outputResult.style.color = "red";
        }
    } catch (error) {
        // Lida com erros de rede ou outros problemas na requisição
        outputResult.textContent = "Erro de conexão com o servidor.";
        outputResult.style.color = "red";
        console.error("Erro ao enviar requisição:", error);
    }
}