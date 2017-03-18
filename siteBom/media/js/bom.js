/**
* Autor: Matheus Rosa
* Data: 05/08/2010
* Descrição: Funções javascript para o site B.O.M
*/

$(function(){
	$('input[type=text]').addClass('input');
	
	var erros = $(".errorlist");
	
	if(erros.length > 0){
		erros.appendTo("#erros");
		$("#erros").show();
	}
	
	$("#bt-sistema").click(function(){
		alert("Ação indisponível no momento!");
		return false;
	});
	
	$("#bt-email").click(function(){
		alert("Ação indisponível no momento!");
		return false;
	})
})

/**
 * Insere uma midia em flash no site
 * 
 * @param url
 * @param altura
 * @param largura
 * @return
 */
function carregarFlash(url, largura, altura) {

	var txt;
	txt = "<object classid=\"clsid:D27cdb6e-ae6d-11cf-96b8-444553540000\" codebase=\"http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=8,0,0,0\" width=\""
			+ largura
			+ "\" height=\""
			+ altura
			+ "\" id=\"flash\" align=\"middle\">";
	txt += "<param name=\"allowScriptAccess\" value=\"sameDomain\" />";
	txt += "<param name=\"movie\" value=\"" + url + "\" />";
	txt += "<param name=\"quality\" value=\"high\" />";
	txt += "<param name=\"wmode\" value=\"transparent\" />";
	txt += "<embed src=\""
			+ url
			+ "\" wmode=\"transparent\" quality=\"high\" bgcolor=\"#ffffff\" width=\""
			+ largura
			+ "\" height=\""
			+ altura
			+ "\" name=\"flash\" align=\"middle\" allowScriptAccess=\"sameDomain\" type=\"application/x-shockwave-flash\" pluginspage=\"http://www.macromedia.com/go/getflashplayer\" />";
	txt += "</object>";

	document.write(txt);

}