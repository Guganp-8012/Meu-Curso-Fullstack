async function verDetalhes(){
  let busca = await fetch("lista-produtos.json")
  let produtos = await busca.json()

  let parametrosURL = new URLSearchParams(window.location.search)
  let idProduto = parametrosURL.get("produtoid")

  let indiceProduto = null
  for (let x in produtos){
    if(produtos[x].id == indiceProduto){
      indiceProduto = x
    }
  }

  document.body.innerHTML = `
  <h3>${produtos[inProduto].nome}</h3> 
  `
}

verDetalhes()