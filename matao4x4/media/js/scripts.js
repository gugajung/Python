/**
 * Abre um popup
 * @param string aURL
 * @param int W
 * @param int L
 */
function abrir(aURL, W, L) {
	window.open(aURL, 'Ler', 'width=' + W + ', height=' + L + ', top=0, left=0, scrollbars=no, status=no, toolbar=no, location=no, directories=no, menubar=no, resizable=no, fullscreen=no');
}
$(document).ready(function(){
	$('#selectacessorios').bind('change',function(){
		var id = $(this).val();
		
		if(id != "")
			location = '/acessorios/' + id;
	});
});

$(document).ready(function(){
		$('#selectveiculos').bind('change',function(){
			var id = $(this).val();
			
			if(id != "")
				location = '/veiculos/' + id;
		});
});


function getFotoMaior(nome){
	$("#fotomaior").html("<img src='/media/"+nome+"' width='300' height='250'  />");	
}

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