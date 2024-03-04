async function verDetalhes(){
  let buscar = await fetch("lista-produtos.json")
  let produtos = await buscar.json()

  let parametrosURL = new URLSearchParams(window.location.search)
  let idProduto = parametrosURL.get("produtoid")

  let indice = null
  for(let x in produtos){
    if(produtos[x].id == idProduto){
      indice = x
    }
  }

  document.body.innerHTML = `
    <h3>${produtos[indice].nome}</h3>
    <img src="${produtos[indice].img}" alt="não renderizou" width="250" height="auto">
    <button><a href="index.html">voltar</a></button>
  `
}

verDetalhes()