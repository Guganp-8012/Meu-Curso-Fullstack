$(document).ready(function(){
    $('#form_ordemservico').submit(function(event){
        let tipo = $('#tipo').val()

        if(tipo == ''){
            alert('Campo obrigatório!')
            event.preventDefault();
        }
    });
});