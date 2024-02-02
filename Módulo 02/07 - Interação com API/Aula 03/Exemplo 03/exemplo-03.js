async function senai(arquivo, id){
    let resposta = await fetch(arquivo)
    let convertido = await resposta.text()
    document.getElementById(id).textContent = convertido
}

senai("compras-do-mes.txt", "t2")
senai("jogos.txt", "p1")