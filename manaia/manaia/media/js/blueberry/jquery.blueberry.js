/*
 * jQuery Blueberry Slider v0.4 BETA
 * http://marktyrrell.com/labs/blueberry/
 *
 * Copyright (C) 2011, Mark Tyrrell <me@marktyrrell.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

(function($){
	$.fn.extend({
		blueberry: function(options) {

			//default values for plugin options
			var defaults = {
				interval: 5000,
				duration: 500,
				lineheight: 1,
				height: 'auto', //reserved
				hoverpause: false,
				pager: true,
				nav: true, //reserved
				keynav: true
			}
			var options =  $.extend(defaults, options);
 
			return this.each(function() {
				var o = options;
				var obj = $(this);

				//armazenar o slide e pager li
				var slides = $('.slides li', obj);
				var pager = $('.pager li', obj);

				//conjunto inicial valores do índice atual e próxima de slides
				var current = 0;
				var next = current+1;

				//ter altura e largura de imagem do slide inicial e calcular proporção de tamanho
				var imgHeight = slides.eq(current).find('img').height();
				var imgWidth = slides.eq(current).find('img').width();
				var imgRatio = imgWidth/imgHeight;

				//define vars for setsize function
				var sliderWidth = 0;
				var cropHeight = 0;

				//esconder todos os slides, desbotam com o primeiro, adicionar classe ativa para o primeiro slide
				slides.hide().eq(current).fadeIn(o.duration).addClass('active');
				

				//construir paginador se já não existe e, se ativado
				if(pager.length) {
					pager.eq(current).addClass('active');
				} else if(o.pager){
					obj.append('<ul class="pager"></ul>');
					slides.each(function(index) {
						$('.pager', obj).append('<li class="tt"><a href="#"><span>'+index+'</span></a></li>')
					});
					pager = $('.pager li', obj);
					pager.eq(current).addClass('active');
				}

				//gire para o slide selecionado no pager clique
				if(pager){
					$('a','.tt', pager).click(function() {
						//stop the timer
						clearTimeout(obj.play);
						//set the slide index based on pager index
						next = $(this).parent().index();
						//rotate the slides
						rotate();
						return false;
						
					});
				}

				//primary function to change slides
				var rotate = function(){
					//fade out current slide and remove active class,
					//fade in next slide and add active class
					slides.eq(current).fadeOut(o.duration).removeClass('active')
						.end().eq(next).fadeIn(o.duration).addClass('active').queue(function(){
							//add rotateTimer function to end of animation queue
							//this prevents animation buildup caused by requestAnimationFrame
							//rotateTimer starts a timer for the next rotate
							rotateTimer();
							$(this).dequeue()
					});

					//update pager to reflect slide change
					if(pager){
						pager.eq(current).removeClass('active')
							.end().eq(next).addClass('active');
					}

					//update current and next vars to reflect slide change
					//set next as first slide if current is the last
					current = next;
					next = current >= slides.length-1 ? 0 : current+1;
				};
				//create a timer to control slide rotation interval
				var rotateTimer = function(){
					obj.play = setTimeout(function(){
						//trigger slide rotate function at end of timer
						rotate();
					}, o.interval);
				};
				//start the timer for the first time
				rotateTimer();

				//pause the slider on hover
				//disabled by default due to bug
				if(o.hoverpause){
					slides.hover(function(){
						//stop the timer in mousein
						clearTimeout(obj.play);
					}, function(){
						//start the timer on mouseout
						rotateTimer();
					});
				}

				//calculate and set height based on image width/height ratio and specified line height
				var setsize = function(){
					sliderWidth = $('.slides', obj).width();
					cropHeight = Math.floor(((sliderWidth/imgRatio)/o.lineheight))*o.lineheight;

					$('.slides', obj).css({height: cropHeight});
				};
				setsize();

				//bind setsize function to window resize event
				$(window).resize(function(){
					setsize();
				});
				
				

				//Add keyboard navigation

				if(o.keynav){
					$(document).keyup(function(e){

						switch (e.which) {

							case 39: case 32: //right arrow & space

								clearTimeout(obj.play);

								rotate();

								break;


							case 37: // left arrow
								clearTimeout(obj.play);
								next = current - 1;
								rotate();

								break;
						}

					});
				}


			});
		}
	});
})(jQuery);
