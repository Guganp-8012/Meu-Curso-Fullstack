$(document).ready(function(){
    $('#form_cliente').submit(function(event){
        let tipo = $('#tipo').val()

        if(tipo == ''){
            alert('Campo obrigatório!')
            event.preventDefault();
        }
    });
});