let urlProdutos = "https://raw.githubusercontent.com/Guganp-8012/Meu-Curso-Fullstack/master/M%C3%B3dulo%2002/07%20-%20Intera%C3%A7%C3%A3o%20com%20API/Consumir%20API/produtos.json"

async function buscar(){
    let resposta = await fetch(urlProdutos)
    let produtos = await resposta.json()

    for (let produto in produtos)
    document.body.innerHTML += `
        <div class="card_produto">
            <img src="${produtos[produto].img}" width="auto" height="320px">

            <h3>
            ${produtos[produto].nome}
            </h3>

            <p>
            ${produtos[produto].descricao}
            </p>

            <div class="valores">
                <h4>
                R$${produtos[produto].valorComDesconto}
                </h4>

                <s>
                R$${produtos[produto].valorSemDesconto}
                </s>
            </div>

            <p>
            ${produtos[produto].tipoEntrega}
            </p>
        </div>
        `
}

buscar()