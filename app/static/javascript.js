(function(win,doc){
    'use strict';
//verifica se o usuario quer mesmo deletar um dado
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseja mesmo apagar?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }

    //ajax do form
    if(doc.querySelector('#form')){
        let form=doc.querySelector('#form');
    
        function sendForm(event)
        {
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN',token);
            ajax.onreadystatechange = function()
            
            {
                if(ajax.status === 0 && ajax.readyState === 0){
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Cadastro realizado!'
                    result.classList.add('alert');
                    result.classList.add('alert-success');
                }
            }
            ajax.send(data);
        }
        form.addEventListener('submit',sendForm,true);
    }
})(window,document);