async function busca(){
  let procura = await fetch("lista-produtos.json") // status response (pesquisar)
  let produtos = await procura.json()

  let listaDiv = document.getElementById("lista-card")
  
  for(let x in produtos){
    listaDiv.innerHTML += `<h1> ${produtos[x].nome} </h1>`
  }
}

busca()