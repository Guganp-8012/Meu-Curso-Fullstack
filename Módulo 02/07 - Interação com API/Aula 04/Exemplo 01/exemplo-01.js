let urlProdutos = "https://raw.githubusercontent.com/Guganp-8012/Meu-Curso-Fullstack/master/M%C3%B3dulo%2002/07%20-%20Intera%C3%A7%C3%A3o%20com%20API/Consumir%20API/produtos.json"

async function buscar(){
    let resposta = await fetch(urlProdutos)
    let produtos = await resposta.json()
    //console.log(produtos[1].descricao)
    for (produto in produtos)
    //document.body.innerHTML += produtos[produto].descricao + "<br>"
    document.body.innerHTML += `
        <div>
            O nome do produto é ${produtos[produto].descricao}
        </div>
        <br>
        `
}

buscar()