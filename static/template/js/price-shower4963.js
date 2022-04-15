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

$('input[name="mat-curtains"]').change(function(){
    updatePrice();
});

(function ($) {

    var methods = {
        init: function (options) {
        	var selectors = {
        		"width":"#dataWidth",
        		"height":"#dataHeight"
        	};
            var width = parseInt($(selectors.width).data('value'));
            var height = parseInt($(selectors.height).data('value'));
            
            console.log(width);
            
            var material = 200;
            // var material = parseInt($(selectors.material).data('price'));
            // var materialName = $(selectors.material).val();
            var message = "";
            
            // var materialInput = $(selectors.dbPrice);
            var dbPrice = 0;
            var dbOldPrice = 0;
            var benefit = 0;

            if(isNaN(width) || width < 1 || isNaN(height) || height < 1){
            	$(this).text('От '+dbPrice);
            	return false;
            }

			var square = width*2*height;
            var totalPrice = square*material/10000;
			
			$('[name="options[price_wallpaper]"]').val(totalPrice);
            totalPrice = Math.ceil(totalPrice);
            totalPrice = 1430;
            console.log(totalPrice);
			totalOldPrice = 2730;
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

            message = "Фотошторы для ванной размером" + width + "x" + height + "см.";
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


