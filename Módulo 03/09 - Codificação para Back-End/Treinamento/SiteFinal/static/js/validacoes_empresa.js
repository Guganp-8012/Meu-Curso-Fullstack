$(document).ready(function(){
    $('#form_empresa').submit(function(event){
        let razao_social = $('#razao_social').val()
        let cnpj = $('#cnpj').val()

        if(razao_social == ''){
            alert('Campo obrigatório!')
            event.preventDefault();
        }

        if(cnpj == ''){
            alert('Campo obrigatório!')
            event.preventDefault();
        }

        if(cnpj != '' && cnpj.length != 14){
            alert('Campo CNPJ não possui 14 caracteres!')
            event.preventDefault();
        }
    });
});