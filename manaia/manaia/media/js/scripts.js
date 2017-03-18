function validaDados(){
	if(document.news.nome.value == ""){
		alert("Não deixe o campo NOME sem ser preenchido.");
		document.news.nome.focus();
		return false;
	}
	if(document.news.email.value == ""){
		alert("Não deixe o campo E-MAIL sem ser preenchido.");
		document.news.email.focus();
		return false;
	}
	return true;
	
}

function abrir() {         

            semx=window.open("","","toolbar=no,location=no,status=no,resizable=no,scrollbars=no,menubar=no,fullscreen=0");

            self.focus();

            semx.moveTo(0,0);

            semx.resizeTo((screen.width-10),screen.height);

            semx.location="/areacliente/";

        }

// function validaBusca(){
	// var q = $("#busca").val();
	// if(q==''){
		// alert('Não foi possível realizar a busca com o campo vazio !\n');
		// return false;
	// }
// 	
	// return true;
// }

