$(document).ready(function(){
    $('#form_servico').submit(function(event){
        let tipo = $('#tipo').val()

        if(tipo == ''){
            alert('Campo obrigatório!')
            event.preventDefault();
        }
    });
});