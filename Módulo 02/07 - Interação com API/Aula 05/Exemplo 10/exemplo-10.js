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

  /*
  for(let card in elementosCards){
    elementosCards[card].addEventListener("click", clicou)
  }
  */

  for(let card of elementosCards){
    card.addEventListener("click", clicou)
  }

}

busca()

function clicou(){
  let produtoId = this.getAttribute("data-id")
  window.location.href = "detahes.html?prod-id=" + produtoId
}