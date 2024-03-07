async function busca(){
  let procura = await fetch("lista-produtos.json") // status response (pesquisar)
  let produtos = await procura.json()

  let listaDiv = document.getElementById("lista-card")
  
  for (let produto of produtos){
  listaDiv.innerHTML += `
    <div class="card" data-id="${produto.id}">
      <div class="grupo-img">
        <img src="${produto.img}" alt="Não renderizou" width="auto" height="auto">
      </div>

      <div class="textos">
        <h3>${produto.nome}</h3>

        <p>${produto.descricao}</p>

        <div>
          <span class="comDesconto">
            R$ ${(produto.valorComDesconto).toFixed(2).replace(".", ",")}
          </span>

          <span class="semDesconto">
            R$ ${(produto.valorSemDesconto).toFixed(2).replace(".", ",")}
          </span>
        </div>
      </div>
    </div>
  `
  }

  let elementosCards = document.querySelectorAll(".card")

  for(let card of elementosCards){
    card.addEventListener("click", cliqueCard)
  }

  // usando o IN a varíavel recebe o índice
  // usando o OF recebe o valor do item
}

busca()

function cliqueCard(){
  let elementoID = this.getAttribute("data-id")
  //alert(elementoID)
  //alert(window.location.href)
  //window.location.href = "http://www.google.com"
  window.location.href = "detalhes.html?produtoid=" + elementoID
}