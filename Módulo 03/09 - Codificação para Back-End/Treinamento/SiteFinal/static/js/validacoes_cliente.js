$(document).ready(function(){
    $('#form_cliente').submit(function(event){
        let nome = $('#nome').val()
        let dataNascimento = $('#data_nascimento').val()

        if(nome == ''){
            alert('Campo obrigatório!')
            event.preventDefault();
        }
        
        if(dataNascimento == ''){
            alert('Campo obrigatório!')
            event.preventDefault();
        }
    });
});