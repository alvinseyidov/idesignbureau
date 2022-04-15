function updatePrice(){
	$('.price_wallpaper').getPrice();
};

$(document).ready(function(){
	updatePrice();
});

$("#dataWidth, #dataHeight").change(function(){
	updatePrice();
});

$('input[name="clamping"]').change(function(){
    updatePrice();
});

$('input[name="size-pillow"]').change(function(){
    updatePrice();
    if ($(this).val() == '40x40'){
        console.log('40x40');
        $('.browsing .mebel.curtains img').attr('src','/upload/pillow/pillow-40x40.png');       
    } else {
        console.log('50x70');
        $('.browsing .mebel.curtains img').attr('src','/upload/pillow/pillow-50x70.png');       
    }
});

(function ($) {

    var methods = {
        init: function (options) {
            var width = $('input[name="size-pillow"]:checked').data('width');
            var height = $('input[name="size-pillow"]:checked').data('height');
            var material = 200;
            var priceSize = $('input[name="size-pillow"]:checked').data('price');
            // var materialName = $(selectors.material).val();
            var message = "";
            
            // var materialInput = $(selectors.dbPrice);
            var dbPrice = 0;
            var dbOldPrice = 0;
            var benefit = 0;

            // if(isNaN(width) || width < 1 || isNaN(height) || height < 1){
            // 	$(this).text('От '+dbPrice);
            // 	return false;
            // }

			// var square = width*2*height;
            var totalPrice = priceSize;
			
			$('[name="options[price_wallpaper]"]').val(totalPrice);
            totalPrice = Math.ceil(totalPrice);
            console.log(priceSize);
			totalOldPrice = Math.ceil(totalPrice / 0.7);
            benefit = totalOldPrice - totalPrice;
            $(this).text(totalPrice);
            // console.log(benefit);
            $('.old-price-wallpaper').text(totalOldPrice + " р.");
			$('#benefit').text("ваша выгода " + benefit + " р.");
			$("input[name='options[price_wallpaper]']").val(totalPrice);

            $('.size_width').text(width);
            $('.size_height').text(height);
            $('input[name="width"]').val(width);
            $('input[name="height"]').val(height);

            message = "Фотоподушка размером" + width + "x" + height + "см.";
            $('.message-order-all[name=message]').text(message);
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


