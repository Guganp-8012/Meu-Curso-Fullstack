let urlJogos = "https://raw.githubusercontent.com/Guganp-8012/Meu-Curso-Fullstack/master/M%C3%B3dulo%2002/07%20-%20Intera%C3%A7%C3%A3o%20com%20API/Aula%2004/Exemplo%2003/exemplo-03.json"

async function buscar(){
    let resposta = await fetch(urlJogos)
    let Jogos = await resposta.json()

    for (let jogo in Jogos)
    document.body.innerHTML += `
        
        <div class="card_produto">
            <h3>
            ${Jogos[jogo].nome}
            </h3>

            <img src="${Jogos[jogo].img}" width="auto" height="100px">
        </div>

    `
}

buscar()