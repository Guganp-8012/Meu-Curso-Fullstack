$(document).ready(function(){
    $('#form_ordemservico').submit(function(event){
        let cliente = $('#cliente').val()
        let servico = $('#servico').val()
        let data = $('#data').val()

        if(cliente == ''){
            alert('Campo obrigatório!')
            event.preventDefault();
        }

        if(servico == ''){
            alert('Campo obrigatório!')
            event.preventDefault();
        }

        if(data == ''){
            alert('Campo obrigatório!')
            event.preventDefault();
        }
    });
});