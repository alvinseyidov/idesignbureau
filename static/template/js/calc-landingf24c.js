$(document).ready(function() {
    //var const_podramnic_price = 340;
    //var const_podramnic_price = 332;
    //var const_podramnic_price = 382;
    var const_podramnic_price = 352;
    //var const_holst_price = 2248;
    var const_holst_price = 2069;
    //var const_holst_price = 1955;
    var const_lak_price = 7000;
    //var const_penokarton_price = [[++price_penokarton]];
    //var const_samokleyka_price = [[++price_samokleyka]];
    var const_penokarton_price = 2800;
    var const_samokleyka_price = 1900;

    function calcPrice(isSet){
        if(isSet == 'holst'){
            console.log('Только холст');
        }
        
        $("option.sel-size").each(function() {
            width = parseInt($(this).attr("data-width"));
            width = width / 100;
            height = parseInt($(this).attr("data-height"));
            height = height / 100;
            area = width * height;
            pricePoster = area * const_holst_price;
            pricePodramnik = (width * 2 + height * 2) * const_podramnic_price;
            if(isSet == 'holst'){
                priceCustomSizeRound = Math.round(pricePoster*2);
            } else {
                priceCustomSizeRound = Math.round((pricePoster + pricePodramnik)*2);
            }
            $(this).text($(this).attr("data-width") + " x " + $(this).attr("data-height") + " - " + priceCustomSizeRound + " р.");
        });
    
        $("li.sel-size").each(function() {
            width = parseInt($(this).attr("data-width"));
            width = width / 100;
            height = parseInt($(this).attr("data-height"));
            height = height / 100;
            area = width * height;
            pricePoster = area * const_holst_price;
            pricePodramnik = (width * 2 + height * 2) * const_podramnic_price;
            if(isSet == 'holst'){
                priceCustomSizeRound = Math.round(pricePoster*2);
            } else {
                priceCustomSizeRound = Math.round((pricePoster + pricePodramnik)*2);
            }
            $(this).text($(this).attr("data-width") + " x " + $(this).attr("data-height") + " - " + priceCustomSizeRound + " р.");
        });
    }



    // $("#lak").attr("disabled", "disabled");
    if ($("#type-2").prop("checked")){
        $('.calc-photo .section.size').hide();
        $('.calc-photo .count-module').show();
    }

    calcPrice();

    $("[name=size]").on("change", function() {
        calcBudget();
    });

    $("[name=lak]").on("change", function() {
        calcBudget();
    });

    $("[name=count-module]").on("change", function() {
        calcBudget();
    });

    $("[name=effect]").on("change", function() {
        calcBudget();
    });

    $("[name=type-product]").on("change", function() {
        if ($(this).is("#type-1") ) {
            $(".section.count-module").hide();
            $(".section.size").show();
            $(".section.price .change-price").show();
            $(".section.price .price-module").hide();

            calcPrice();
        } else if ($(this).is("#type-2")) {
            $(".section.size").hide();
            $(".section.count-module").show();
            $(".section.price .change-price").hide();
            $(".section.price .price-module").show();

        } else if ($(this).is("#type-3")) {
            $(".section.count-module").hide();
            $(".section.size").show();
            $(".section.price .change-price").show();
            $(".section.price .price-module").hide();
            $("#holst").prop("checked", "checked");
            $("#lak").removeAttr("disabled");
            $(".title-lak").css("color", "#000");

            calcPrice('holst');
        }
        calcBudget();
    });

    function calcBudget(isSet) {
        var totalPrice = '';
        var priceLak = '';
        var result = '';
        var width = parseInt($("[name=size]").find("option:selected").attr("data-width"));
        var dwidth = width / 100;
        var height = parseInt($("[name=size]").find("option:selected").attr("data-height"));
        var dheight = height / 100;
        var area = dwidth * dheight;
        var countModule = parseInt($("[name=count-module]").val());
        var typeProduct = $("[name=type-product]:checked").val();
        var material = $("[name=type-canvas]:checked").val();
        var maket = $("[name=maket]:checked").val();
        var priceEffect = parseInt($("[name=effect]").find("option:selected").attr("data-price"));
        var nameEffect = $("[name=effect]").find("option:selected").attr("value");

        console.log("width = "+dwidth+'\n' + "height = "+dheight+'\n' + "area = "+area+'\n');

        if ($("#type-1").prop("checked")) {
            pricePoster = area * const_holst_price;
            pricePodramnik = (dwidth * 2 + dheight * 2) * const_podramnic_price;
            var priceCustomSize = pricePoster + pricePodramnik;
            var priceCustomSizeRound = Math.round(priceCustomSize*2);
            $(".select-size .jq-selectbox__select-text").text(width + " x " + height + " - " + priceCustomSizeRound + " р.");

        }  else if ($("#type-2").prop("checked")) {
            var area = 0.2 * 0.2;
            area = countModule * area;
            pricePoster = area * const_holst_price;
            pricePodramnik = (dwidth * 2 + dheight * 2) * const_podramnic_price * countModule;
            var priceCustomSizeRound = Math.round((pricePoster + pricePodramnik)*2);

        } else if ($("#type-3").prop("checked")) {
            pricePoster = area * const_holst_price;
            var priceCustomSizeRound = Math.round(pricePoster*2);
            $(".select-size .jq-selectbox__select-text").text(width + " x " + height + " - " + priceCustomSizeRound + " р.");
        }
        
        console.log('pricePoster -'+pricePoster);
        console.log('pricePodramnik -'+pricePodramnik);
        console.log(const_holst_price);
        console.log(const_podramnic_price);
        console.log(priceCustomSizeRound);

        if ($("#lak").prop("checked")) {
            var priceLak = Math.round(area * const_lak_price);
        } else {
            priceLak = 0;
        }

        //console.log(priceCustomSizeRound);

        //console.log(area+"*"+const_penokarton_price+"+"+area+"*"+const_samokleyka_price+"="+priceCustomSize);

        totalPrice = parseInt(priceCustomSizeRound);
        totalPrice += parseInt(priceLak);
        totalPrice += parseInt(priceEffect);
        $(".section.price .change-price span").text(totalPrice);
        $(".section.price .price-module").text("От " + totalPrice + " р.");
        $("[name='options[material]']").attr("value", material);
        $("[name='options[width]']").attr("value", width);
        $("[name='options[height]']").attr("value", height);
        $("[name='options[lak]']").attr("value", priceLak);
        $("[name='options[total_price]']").attr("value", totalPrice);

        result += "\n";
        result += "Тип продукта: " + typeProduct + "\n";
        // result += "Ширина:" + width + "\n";
        // result += "Высота:" + height + "\n";
        result += "Обработка лаком: " + priceLak + "\n";
        result += "Обработка фото: " + nameEffect + "\n";
        result += "Когда макет: " + maket + "\n";
        // result += "Итоговая цена: " + totalPrice + "\n";

        $("[name=message]").text(result);

        //console.log(typeProduct+" - "+ width+" - "+height+" - "+priceLak+" - "+totalPrice);

    }

    calcBudget();
});