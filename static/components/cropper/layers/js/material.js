var idx = 1;
var idxsel = 1;
var sliderFlag = 0;

$('.slider-example-wallpaper').slick({
    adaptiveHeight: true    
});

$('.type_wallpaper_slider .menu ul > li > ul > li').each(function(){
    $(this).attr('data-id',idx);
    idx++;
});

$('ul.select-material > li.sel-material').each(function(){
    $(this).attr('data-id',idxsel);
    idxsel++;
});

$(document).on("change", "#elLatex", function(val) {
    if ($('[name="options[latex]"]').prop("checked")){
        $('.ilatex').prop('checked', true);
    } else{
        $('.ilatex').prop('checked', false);
    }
    updatePrice();
});


/*Dropdown Menu*/
$('.dropdown').click(function () {
    $(this).attr('tabindex', 1).focus();
    $(this).toggleClass('active');
    $(this).find('.dropdown-menu').slideToggle(300);
});
$('.dropdown').focusout(function () {
    $(this).removeClass('active');
    $(this).find('.dropdown-menu').slideUp(300);
});
$('.dropdown .dropdown-menu li.sel-material').click(function (e) {
    // e.stopPropagation();
    // e.preventDefault();
    var index = $(this).data('id');
    console.log('start-sel - '+index);
    $('.slider').trigger('to.owl.carousel', index-1);
    if(!$('#mat-'+index).prop('checked')){
        $('.addLayout[data-idx="'+index+'"]').trigger('click');
    }
    $(this).parents('.dropdown').find('span').text($(this).text());
    $(this).parents('.dropdown').find('input').attr('value', $(this).attr('id'));
});
/*End Dropdown Menu*/

$(document).on('click', '.type_wallpaper_slider .menu ul > li > ul > li', function(e){
    console.log('start');
    e.stopPropagation();
    e.preventDefault();
    $('.type_wallpaper_slider .menu ul > li > ul > li').removeClass('current');
    $(this).addClass('current');
    var index = $(this).data('id');
    $('.slider-example-wallpaper').slick('slickGoTo', index-1, true);
    if(!$('#mat-'+index).prop('checked')){
    	$('.addLayout[data-idx="'+index+'"]').trigger('click');
    }
});

$('.slider-example-wallpaper').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
    var $menu_item = $('.type_wallpaper_slider .menu ul > li > ul > li');
    var $menu_item_sel = $('.dropdown-menu li.sel-material');
    var $select_text = $('.wrrp-select-material .select span');
    
    var item = nextSlide;
    console.log("Номер слайда - "+ nextSlide);
    
    $menu_item.eq(item).trigger('click');
    $select_text.text($menu_item_sel.eq(item).text());
});

$(".addLayout").click(function(){
	$("#"+$(this).attr("for")).prop('checked', true);
	$parent = $(this).parent();
	
	updatePrice();
	var $current_item = $('.type_wallpaper_slider .menu ul > li > ul > li.current');
	if($current_item.data('id') != $(this).data('idx')){
		$('.type_wallpaper_slider .menu ul > li > ul > li[data-id="'+$(this).data('idx')+'"]').trigger('click');
	}
	$('.mat-info .material_text').text($(this).data('name'));
    $('.mat-price .old-price span').text($(this).data('oldprice'));
    $('.mat-price .price span').text($(this).data('price'));
});

$("#dataWidth, #dataHeight").keyup(function(){
	$(".mebel-free").trigger("click");
	$(".mebel img").attr("src","");
	updatePrice();
});

function updatePrice(){
	$('.price_wallpaper').getPrice();
};

$(document).ready(function(){
	updatePrice();
});
$(document).on('change', '#elLak', function(){
	updatePrice();
});

(function ($) {

    var methods = {
        init: function (options) {
        	var selectors = {
        			"width":"#dataWidth",
        			"height":"#dataHeight",
        			"dbPrice":".input-material:checked",
        			"latex":"#elLatex",
        			"lak":"#elLak"
        	};
            var width = parseInt($(selectors.width).val());
            var height = parseInt($(selectors.height).val());
            var materialInput = $(selectors.dbPrice);
            var dbPrice = 0;
            var checkLatex = null;
            if(materialInput.length){
            	dbPrice = $('[for="'+materialInput.attr('id')+'"]').data('price');
            	checkLatex = $('[for="'+materialInput.attr('id')+'"]').data('latex');
            }else{
            	dbPrice = $('.mat-select > div:first label').data('price');
            }
            
            if(checkLatex){
			    $('#selectLatex').removeClass('hidden');
			    $('.add-latex').removeClass('hidden');
			    $('.option-product.latex .hidden-text').show();
			} else {
			    $('#selectLatex').addClass('hidden');
			    $('.add-latex').addClass('hidden');
			    $(selectors.latex).prop('checked', false);
			    $('.ilatex').prop('checked', false);
			    $('.option-product.latex .hidden-text').hide();
			}
            
            var lak = $(selectors.lak).attr('data-price');
            var latex = $(selectors.latex).attr('data-price');
            if(isNaN(width) || width < 1 || isNaN(height) || height < 1){
            	$(this).text('От '+dbPrice);
            	return false;
            }
			var square = width*height;
            $('#area').text(square/10000);
			var totalPrice = square*dbPrice/10000;
			if($(selectors.lak).prop('checked')){
				totalPrice += square*lak/10000;
			}
			if($(selectors.latex).prop('checked')){
                totalPrice += square*latex/10000;
				//totalOldPrice += square*latex/10000;
			}
			
			$('[name="options[price_wallpaper]"]').val(totalPrice);
			totalPrice = Math.ceil(totalPrice);
			$(this).text(totalPrice);
			$("input[name='options[price_wallpaper]']").val(totalPrice);
        }

    };

    $.fn.getPrice = function (method) {
        // логика вызова метода
        if (methods[method]) {
            return methods[ method ].apply(this, Array.prototype.slice.call(arguments, 1));
        } else if (typeof method === 'object' || !method) {
            return methods.init.apply(this, arguments);
        } else {
            $.error('Метод с именем ' + method + ' не существует для jQuery.canvas');
        }
    };

})(jQuery);