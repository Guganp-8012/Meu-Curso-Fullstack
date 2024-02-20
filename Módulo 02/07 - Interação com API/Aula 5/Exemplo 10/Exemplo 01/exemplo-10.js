async function busca(){
  let procura = await fetch("lista-produtos.json") // status response (pesquisar)
  let produtos = await procura.json()

  let listaDiv = document.getElementById("lista-card")
  
  for (let produto of produtos)
  document.body.innerHTML += `
    <div class="card">
      <img src="${produto.img}" alt="Não renderizou" width="auto" height="150">
      
      <p class="titulo">
        ${produto.nome}
      </p>

      <p>
        ${produto.descricao}
      </p>

      <div class="valores">
        <span class="valorCom">
          R$ ${(produto.valorComDesconto).toFixed(2).replace(".", ",")}
        </span>

        <span class="valorSem">
          R$ ${(produto.valorSemDesconto).toFixed(2).replace(".", ",")}
        </span>
      </div>
    </div>
  `
}


busca()