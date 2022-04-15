/**
 * Gr8Dev gr8dev.com
 * @author Eugeny Nosenko info@gr8dev.com
 * @version 1.0
 */


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
        		"height":"#dataHeight",
                "material":"input[name='mat-curtains']:checked",
                "clamping":"input[name='clamping']:checked"
        	};
            var width = parseInt($(selectors.width).val());
            var height = parseInt($(selectors.height).val());
            var material = parseInt($(selectors.material).data('price'));
            var materialName = $(selectors.material).val();
            var clamping = parseInt($(selectors.clamping).data('price'));
            var clampingName = $(selectors.clamping).val();
            var message = "";

            var materialInput = $(selectors.dbPrice);
            var dbPrice = 0;
            var dbOldPrice = 0;
            var benefit = 0;

            if(isNaN(width) || width < 1 || isNaN(height) || height < 1){
            	$(this).text('От '+dbPrice);
            	return false;
            }

			var square = width*2*height;
            var totalPrice = (square*material/10000)+clamping;
			
			$('[name="options[price_wallpaper]"]').val(totalPrice);
            totalPrice = Math.ceil(totalPrice);
			totalOldPrice = Math.ceil(totalPrice * 1.4);
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
            $('.material_text').text(materialName);
            $('.clamping_text').text(clampingName);
            message = "Материал:" + materialName + "\n" + "Крепление к карнизу:" + clampingName + "\n";
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


