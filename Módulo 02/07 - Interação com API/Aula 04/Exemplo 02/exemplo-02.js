let urlProdutos = "https://raw.githubusercontent.com/Guganp-8012/Meu-Curso-Fullstack/master/M%C3%B3dulo%2002/07%20-%20Intera%C3%A7%C3%A3o%20com%20API/Consumir%20API/produtos.json"

async function buscar(){
    let resposta = await fetch(urlProdutos)
    let produtos = await resposta.json()
    for (let produto in produtos)
    document.body.innerHTML += `
        <div class="card_produto">
            <img src="${produtos[produto].img}" width="auto" height="250px">

            <h3>
            ${produtos[produto].nome}
            </h3>
            
            <br>

            <s>
            ${produtos[produto].descricao}
            </s>

            <br>

            <h4>
                ${produtos[produto].valorComDesconto}

                <s class="sem_desconto_id">
                ${produtos[produto].valorSemDesconto}
                </s>
            </h4>

            <br>

            <p>
            ${produtos[produto].tipoEntrega}
            </p>
        </div>
        <br>
        `
}

buscar()