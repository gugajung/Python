
/**
 * 
 * @returns
 */
function iniciaTransicao(){
	$('#bloco-tld').cycle({
		speed: 'slow',
		timeoutFn: timeout
	});
	$('#bloco-bld').cycle({
		speed: 'slow',
		timeoutFn: timeout2
	});
	$('#bloco-mld').cycle({
		speed: 'slow',
		timeoutFn: timeout3
	});
}

/**
 * 
 * @param currElement
 * @param nextElement
 * @param opts
 * @param isForward
 * @returns
 */
function timeout(currElement, nextElement, opts, isForward){
	return calculaTempoBanners(
	parseInt($(this).attr('tempo')), 
	$("#banners #bloco-tld img"), opts);
}

/**
 * 
 * @param currElement
 * @param nextElement
 * @param opts
 * @param isForward
 * @returns
 */
function timeout2(currElement, nextElement, opts, isForward){
	return calculaTempoBanners(
	parseInt($(this).attr('tempo')), 
	$("#banners #bloco-mld img"), opts);
}

/**
 * 
 * @param currElement
 * @param nextElement
 * @param opts
 * @param isForward
 * @returns
 */
function timeout3(currElement, nextElement, opts, isForward){
	return calculaTempoBanners(
	parseInt($(this).attr('tempo')), 
	$("#banners #bloco-bld img"), opts);
}

/**
 * Calcula o tempo para os banners
 * @param banners
 * @returns
 */
function calculaTempoBanners(tempo, banners, opts){
	var ids, totalIds, time;
	
	ids = new Array();
	
	banners.each(function(){
		id = $(this).attr("banner");
		ids.push(id);
	});
	
	totalIds = ids.length;
	time = calculaTempo(tempo, totalIds, opts);
	
	return time;
}

/**
 * Calcula o tempo para cada banner
 * @param tempo
 * @param total
 * @param opts
 * @returns
 */
function calculaTempo(tempo, total, opts){
	var tempo_,index;
	for(i = 0; i < total; i++){
		index = opts.currSlide;
		
		if(index == i)
			tempo_ = tempo * 1000;
	}
	return tempo_;
}
/**
 * 
 * @param id
 * @returns
 */
function infoVideo(id){
	

	// $('#info-video').ajaxStart(function(){
// 		
		// $(this).dialog({
			// title: 'Carregando...',
			// width: 1020,
			// draggable: true,
			// position: 'top'
		// });
// 		
		// $(this).html("<img src='/midias/imgs/ajax-loader.gif' width='32' height='32' alt='Carregando..' />");
	// });

	$.ajax({
		type: 'GET',
		url: '/info_video/' + id +'/',
		data: '',
		dataType: 'json',
		success: function(retorno){
			 $.each(retorno, function(i, item){
				 
				 titulo = item.fields.titulo;
				 ano = (item.fields.ano != null) ? item.fields.ano : '';
				 capa = item.fields.capa;
				 codigo = item.fields.codigo;
//				 descricao = item.fields.descricao;
//				 genero = item.fields.genero;
				
				 // $("#info-video").dialog({title: codigo  + ' - ' + titulo + ' - ' + ano});		
				 	// $("#info-video").css('display','block');	
				 $('#info-video').html('<img src="/midias/'+capa+'"/>');
				 
			 });
		}
	});
}

$(document).ready(function(){
	
	$('#curriculum-online button').click(function(){
		alert('A��o indispon�vel no momento!');
		return false;
	});
	
	var erros = $(".errorlist");
	if(erros.length > 0){
		erros.appendTo("#erros");
		$("#erros").show();
	}
	
	$("#tb-frm-contato input[type=text]").addClass("texto");
	
	if ( $("#lista-lojas") ) {
		$("#lista-lojas").cycle({
			fx: 'fade'
		})
	}
});

/**
 * Envia o form para listar os generos
 * @return 
 */
function listaGeneros(){
	$("#filtroGenero").submit();
}

/**
 * Valida o campo busca
 * @returns {Boolean}
 */
function validaBusca(){
	if($("#buscar").val()==''){
		alert('Não é possivel fazer a pesquisa com o campo vazio!\n');
		return false;
	}
	
	return true;
}

function getNoticiasFecomercio(){
	// mostro o 'loader' de carregando
	$(".loader").html("<img src='/midias/imgs/ajax-loader.gif' />");

	// pego os dados em xml
	$.get('/xml/', '', function(dados){
		
		// limpo a div para receber os links
		$('.loader').hide();
		
		// crio uma lista que ira receber os links
		var links = new Array();
		
		// para cada item encontrado
		$(dados).find('item').each(function(){
			// pego o titulo
			var titulo = $(this).find('title').text();
			// pego a url
			var url = $(this).find('link').text();
			// adiciono o html montado com a URL e o TITULO	
			links.push('<li><a href="'+url+'" target="_blank">'+titulo.slice(0,60)+'...</a></li>');
				
		});
		
		// adiciono os 6 �ltimos links em html na lista <ul></ul>
		$('#noticias_fecomercio').html(links.slice(0,6).join(''));
		}, 'xml');
}