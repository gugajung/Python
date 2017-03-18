 $(document).ready(function() {
 
	$(".categoriaMenu").click(function(){
		$("#valorCategoria").val($(this).attr("id"))		
		$.ajax({
			url : "/areacliente/arquivos/",
			data : $("#menuConsultaForm").serialize(),
			type : 'POST',
			dataType : 'json',
			success : function(dados) {
				var html = ""
				if (dados.length > 0) {
					for (var i=0; i < dados.length; i++) {
							
						html += "<li><a href=/media/"+dados[i].fields["arquivo"]+" target='_blank' class='linksDownload'>"+dados[i].fields["nome"]+"</a></li>";
							
					};
				} else{
						html ="<div id='nenhumEncontrado' align='center'>Nenhum arquivo foi encontrado</div>"
				};		
				$("#documentosConsultaDownload").html(html);	
			}
		});
	});
	
	$("#btnPesquisarDownloads").click(function(){ 
				$.ajax({
					url : "/areacliente/pesquisar/",
					data : $("#pesquisaForm").serialize(),
					type : 'POST',
					dataType : 'json',
					success : function(dados) {
						var html = ""
						if (dados.length > 0) {
							for (var i=0; i < dados.length; i++) {									
								
								html += "<li><a href=/media/"+dados[i].fields["arquivo"]+" target='_blank' class='linksDownload'>"+dados[i].fields["nome"]+"</a></li>";	
							};
						} else{
								html ="<div id='nenhumEncontrado' align='center'>Nenhum arquivo foi encontrado</div>"
						};
						$("#documentosConsultaDownload").html(html);	
					}
		});
 	});
});