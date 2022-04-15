$('.wrrp-quick-order .tab-link .item').on("click", function(){
    var tab = $(this).data('tab');
    console.log(tab);
    $('.wrrp-quick-order .tab-link .item').removeClass('active');
    $(this).addClass('active');
    $('.wrrp-quick-order .tab-content').hide();
    $('.'+tab).fadeIn();
    $('html,body').animate({scrollTop:$('#startOrder').offset().top-55+"px"},{duration:1E3});
});
    
$('.show-material').on("click", function(){
    $('.wrrp-quick-order .mat-wrrp .mat-select .item').fadeIn();
    $(this).hide();
});

$(".glue label").click(function(){
	if ($('[name="options[glue]"]').prop("checked")){
        $(".message-order-all[name=message]").text("");
    } else{
        $(".message-order-all[name=message]").text("Положить клей");
    }
});

$(document).on("change", "#elDiscount", function(val) {
    if ($('[name="options[discount]"]').prop("checked")){
        $(this).val("Согласны оплатить заказ на сайте и Получить скидку в 3%");        
    } else{
        $(this).val("");
    }
});

$(document).on("change", "#elLatex", function(val) {
    if ($('[name="options[latex]"]').prop("checked")){
        $('.ilatex').prop('checked', true);
    } else{
        $('.ilatex').prop('checked', false);
    }
    updatePrice();
});

/* Валидация полей размера */
$(document).on("change", "#dataWidth", function(val) {
    this.value=this.value.replace(/[^0-9]+/g, '');
    iswidth(this);
});

$(document).on("change", "#dataHeight", function(val) {
    this.value=this.value.replace(/[^0-9]+/g, '');
    isheight(this);
});

$(document).on("keyup", "#dataWidth", function(val) {
    this.value=this.value.replace(/[^0-9]+/g, '');
});

$(document).on("keyup", "#dataHeight", function(val) {
    this.value=this.value.replace(/[^0-9]+/g, '');
});

function iswidth(obj) {
    if (obj.value>1500) obj.value=1500;
    if (obj.value<10) obj.value=10;
}

function isheight(obj) {
    if (obj.value>1500) obj.value=1500;
    if (obj.value<10) obj.value=10;
}

$( ".wall-params .dost input" ).focus(function() {
    if ( $(this).val() == 0 ){
        $(this).val( "" );
    }
});

$( ".wall-params .dost input" ).focusout(function(){
    if ( $(this).val() == 0 ){
        $(this).val( 0 );
    }
});

var idx = 1;
//var currentElem = '';
var sliderFlag = 0;

if($(".browsing .img img").is("#image")){
    $(".show-review").click(function(){
        var canv = $("#image").cropper("getCroppedCanvas");
        $("#imgCropper").attr('src', canv.toDataURL('image/jpeg'));
        $('#infoWidth').text($('#dataWidth').val());
        $('#infoHeight').text($('#dataHeight').val());
    });
} else {
    $(".show-review").click(function(){
        var canv = $("#uploaded_image").cropper("getCroppedCanvas");
        $("#imgCropper").attr('src', canv.toDataURL('image/jpeg'));
        $('#infoWidth').text($('#dataWidth').val());
        $('#infoHeight').text($('#dataHeight').val());
    })
}


$('.slider-example-wallpaper').slick({
    adaptiveHeight: true    
});


$('.show-modal-material').click(function(){
    $(this).parent().trigger('click');
    $.fancybox.open({
    	src  : '#parent_popup_material',
    	type : 'inline',
    	opts : {
    		afterLoad : function(){
                $('.slider-example-wallpaper').slick('refresh');
                var url = $(this.element).data('url');
                if(url){
                    $.fancybox.wrap.find('[name="link_product"]').val(url);
                }
            }
    	}
    });
});
    
$('.fancybox_material').fancybox({
    afterLoad : function(){
        $('.slider-example-wallpaper').slick('refresh');
        var url = $(this.element).data('url');
        if(url){
            $.fancybox.wrap.find('[name="link_product"]').val(url);
        }
    }
});

$('.type_wallpaper_slider .menu ul > li > ul > li').each(function(){
    $(this).attr('data-id',idx);
    idx++;
});

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
    var item = nextSlide;
    console.log("Номер слайда - "+ nextSlide);
    
    $menu_item.eq(item).trigger('click');
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

function updatePrice(){
	$('.price_wallpaper').getPrice();
};

$(document).ready(function(){
	//$('.mat-select .item:first label').trigger('click');
	updatePrice();
});
$(document).on('change', '#elLak', function(){
	updatePrice();
});
$(document).on('change', '#elGlue', function(){
    updatePrice();
});

$(document).on('change', '#elDiscount', function(){
    updatePrice();
});




$("#dataWidth, #dataHeight").keyup(function(){
	$(".mebel-free").trigger("click");
	$(".mebel img").attr("src","");
	updatePrice();
});

(function ($) {

    var methods = {
        init: function (options) {
        	var selectors = {
        			"width":"#dataWidth",
        			"height":"#dataHeight",
        			"dbPrice":".input-material:checked",
        			"upperprice":"#upperprice",
        			"lak":"#elLak",
                    "glue":"#elGlue",
                    "latex":"#elLatex",
                    "discount":"#elDiscount",
                    "currency":"#currency"
        	};
            var width = parseInt($(selectors.width).val());
            var height = parseInt($(selectors.height).val());
            var currency = $(selectors.currency).val();
            var materialInput = $(selectors.dbPrice);
            var dbPrice = 0;
            var dbOldPrice = 0;
            var benefit = 0;
            var checkLatex = null;
            
            if(materialInput.length){
                dbPrice = $('[for="'+materialInput.attr('id')+'"]').data('price');
            	dbOldPrice = $('[for="'+materialInput.attr('id')+'"]').data('oldprice');
            	checkLatex = $('[for="'+materialInput.attr('id')+'"]').data('latex');
            	console.log('checkLatex - ' + checkLatex);
            }else{
                dbPrice = $('.mat-select > div:first label').data('price');
            	dbOldPrice = $('.mat-select > div:first label').data('oldprice');
            }
            
            if($(selectors.upperprice).prop('checked')){
                dbPrice += Number($(selectors.upperprice).val());
				dbOldPrice += Number($(selectors.upperprice).val());
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
            var totalPrice = square*dbPrice/10000;
			var totalOldPrice = square*dbOldPrice/10000;
			
			if (totalOldPrice == 0){
			    var removeOldPrice = 1;
			}

			if($(selectors.lak).prop('checked')){
                totalPrice += square*lak/10000;
				totalOldPrice += square*lak/10000;
			}
			
			if($(selectors.latex).prop('checked')){
                totalPrice += square*latex/10000;
				totalOldPrice += square*latex/10000;
			}
            
			$('[name="options[price_wallpaper]"]').val(totalPrice);
            totalPrice = Math.ceil(totalPrice);
			totalOldPrice = Math.ceil(totalOldPrice);
            if($(selectors.glue).prop('checked')){
                // console.log($(selectors.glue).data('price'));
                totalPrice += $(selectors.glue).data('price');
                totalOldPrice += $(selectors.glue).data('price');
            }
            
            if($(selectors.discount).prop('checked')){
                console.log('Старая цена - ' + totalOldPrice);
                if (removeOldPrice){
                    totalOldPrice = totalPrice;
                }
                totalPrice = Math.ceil(totalPrice *0.97);
            } else {
                
            }
            
            // if ($('#type-product').val() == 'ready'){
            //     totalPrice = $('#price-product').val();
            //     if($('#old-price-material').val()){
            //         totalOldPrice = $('#old-price-material').val();
            //     } else {
            //         totalOldPrice = $('#price-material').val();
            //     }
            // }
            
            benefit = totalOldPrice - totalPrice;    
            
            $(this).text(totalPrice);
            // console.log(benefit);
            console.log(removeOldPrice);
            if (removeOldPrice == 1){
			    $('.old-price-wallpaper').text("");
			} else {
			    $('.old-price-wallpaper').html('<div class="ttl">Без скидки</div> <div class="insert">' + totalOldPrice + ' ' + currency +'</div>');    
			}
            
            if(benefit > 0){
                $('.browsing2 .benefit').html('<div class="ttl">Ваша выгода</div> <div class="insert">' + benefit + ' ' + currency+'</div>');    
            } else {
                $('.browsing2 .benefit').text('');
            }
			$("input[name='options[price_wallpaper]']").val(totalPrice);
			
			$('.popup_callback_one_click .size_height').text(height);
			$('.popup_callback_one_click .size_width').text(width);
			$('.popup_callback_one_click .material_text').text($('.input-material[name="options[material]"]:checked').val());
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