async function detalhes(){
  let procura = await fetch("lista-produtos.json")
  let produtos = await procura.json()

  let parametrosURL = new URLSearchParams(window.location.search)
  let idProduto = parametrosURL.get("produtoid")

  let indice = null
  for (let x in produtos){
    if (produtos[x].id == idProduto){
      indice = x
    }
  }

  document.title = produtos[indice].nome

  document.body.innerHTML += `
    <h1>${produtos[indice].nome}</h1>

    <img src="${produtos[indice].img}" alt="não renderizou" width="300" height="auto" style="border: 1px solid #000; border-radius: 10px">

    <p>${produtos[indice].descricao}</p>

    <div class="valores">
      <span class="com-desconto">
        R$ ${(produtos[indice].valorComDesconto).toFixed(2).replace(".", ",")}
      </span>

      <span class="sem-desconto">
        R$ ${(produtos[indice].valorSemDesconto).toFixed(2).replace(".", ",")}
      </span>
    </div>
  `
}

detalhes()