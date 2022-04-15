var $image = $(selectors.image);
var options;
options = {
        // aspectRatio: 16 / 9,
        autoCrop: false,
        //preview: '.img-preview',
        zoomable: false,
        viewMode: 1,
        dragMode: 'none',
        autoCropArea: 1,
        movable: false,
        guides:false,
        //scalable: false,
        toggleDragModeOnDblclick: false,
    };
$(document).ready(function () {
//------------------------------------------------------------------------------
//Не забываем подключать файл опций
//------------------------------------------------------------------------------

    let vertical = false;
    let originalUrl = '';

var cmPixelSize = 0;
var cropStartWidth;
var cropStartHeight;

function showLeftRight(isShow) {
    if (isShow)
        $(".line-e, .line-w, .point-e, .point-w").show();
    else
        $(".line-e, .line-w, .point-e, .point-w").hide();
}

function showTopBottom(isShow) {
    if (isShow)
        $(".line-n, .line-s, .point-n, .point-s").show();
    else
        $(".line-n, .line-s, .point-n, .point-s").hide();
}

function calculateCover(frame, sides) {
    var ratio = sides[1] / sides[0],
        cover = { 
            width: frame.width,
            height: Math.ceil(frame.width * ratio) 
        };

    if (cover.height <= frame.height) {
        cover.height = frame.height;
        cover.width = Math.ceil(frame.height / ratio);
    }

    return cover;
}



function fullBleed(boxWidth, boxHeight, imgWidth, imgHeight) 
{
    // Calculate new height and width
    var initW = imgWidth;
    var initH = imgHeight;
    var ratio = initH / initW;

    imgWidth = boxWidth;
    imgHeight = boxWidth * ratio;

    if(imgHeight > boxHeight){
        imgHeight = boxHeight;
        imgWidth = imgHeight / ratio;
    }
    //  Return new size
    return {
        width: imgWidth,
        height: imgHeight
    };

}

//cropper part
    var console = window.console || {log: function () {}};
    var URL = window.URL || window.webkitURL;


   

    var $download = $('#download');
   
    
    var originalImageURL = $image.attr('src');
    var uploadedImageURL;


    // Tooltip
    // $('[data-toggle="tooltip"]').tooltip();
    // Cropper
        $image.cropper(options);
    
    
    
    
    $image.on('cropstart.cropper', function (e) {
        var cropBoxData = $(this).cropper('getData');

        cropStartWidth = Math.round(cropBoxData.width);
        cropStartHeight = Math.round(cropBoxData.height);
    });
    
    $image.on('cropend.cropper', function (e) {
           
        var cropBoxData = $(this).cropper('getData');
        var getImageData = $(this).cropper('getImageData');

        var oW = parseFloat(getImageData.naturalWidth);
        var oH = parseFloat(getImageData.naturalHeight);

        var cW = Math.round(cropBoxData.width);
        var cH = Math.round(cropBoxData.height);


        var pW = Math.round($(selectors.dataWidth).val());
        var pH = Math.round($(selectors.dataHeight).val());



        var nW = pW + Math.round((cW-cropStartWidth)/cmPixelSize);
        var nH = pH + Math.round((cH-cropStartHeight)/cmPixelSize);


        $(selectors.dataWidth).val(nW);
        $(selectors.dataHeight).val(nH);


        showLeftRight(false);
        showTopBottom(false);

        if(cW == oW){
            showTopBottom(true);
        }

        if(cH == oH){
            showLeftRight(true);
        }

        //return;
        if (typeof updatePrice !== "undefined") {
            updatePrice();
        }
        //miniShop2.Utils.changePrice();
    });

    // Buttons
    if (!$.isFunction(document.createElement('canvas').getContext)) {
        $('button[data-method="getCroppedCanvas"]').prop('disabled', true);
    }

    if (typeof document.createElement('cropper').style.transition === 'undefined') {
        $('button[data-method="rotate"]').prop('disabled', true);
        $('button[data-method="scale"]').prop('disabled', true);
    }


    // Download
    if ($download.length===0 || typeof $download[0].download === 'undefined') {
        $download.addClass('disabled');
    }


   

    // Methods
    $('.docs-buttons').on('click', '[data-method]', function () {
        var $this = $(this);
        var data = $this.data();
        var $target;
        var result;

        if ($this.prop('disabled') || $this.hasClass('disabled')) {
            return;
        }

        if ($image.data('cropper') && data.method) {
            data = $.extend({}, data); // Clone a new one

            if (typeof data.target !== 'undefined') {
                $target = $(data.target);

                if (typeof data.option === 'undefined') {
                    try {
                        data.option = JSON.parse($target.val());
                    } catch (e) {
                        console.log(e.message);
                    }
                }
            }

            if (data.method === 'rotate') {
                $image.cropper('clear');
            }

            result = $image.cropper(data.method, data.option, data.secondOption);

            if (data.method === 'rotate') {
                $image.cropper('crop');
            }

            switch (data.method) {
                case 'scaleX':
                case 'scaleY':
                    $(this).data('option', -data.option);
                    break;

                case 'getCroppedCanvas':
                    if (result) {

                        // Bootstrap's Modal
                        $('#getCroppedCanvasModal').modal().find('.modal-body').html(result);

                        if (!$download.hasClass('disabled')) {
                           
                            $download.attr('href', result.toDataURL('image/jpeg'));
                        }
                    }

                    break;

                case 'destroy':
                    if (uploadedImageURL) {
                        URL.revokeObjectURL(uploadedImageURL);
                        uploadedImageURL = '';
                        $image.attr('src', originalImageURL);
                    }

                    break;
            }

            if ($.isPlainObject(result) && $target) {
                try {
                    $target.val(JSON.stringify(result));
                } catch (e) {
                    console.log(e.message);
                }
            }

        }
    });


   
    // Import image
    var $inputImage = $('#inputImage');

    if (URL) {
        $inputImage.change(function () {
            $(selectors.fitCropper).prop('checked', false);
            $(selectors.cropToArea).prop('checked', false);
            var files = this.files;
            var file;

            if (!$image.data('cropper')) {
                return;
            }

            if (files && files.length) {
                file = files[0];

                if (/^image\/\w+$/.test(file.type)) {
                    if (uploadedImageURL) {
                        URL.revokeObjectURL(uploadedImageURL);
                    }

                    uploadedImageURL = URL.createObjectURL(file);
                    $image.cropper('destroy').attr('src', uploadedImageURL).cropper(options);
                    $inputImage.val('');
                } else {
                    window.alert('Please choose an image file.');
                }
            }
        });
    } else {
        $inputImage.prop('disabled', true).parent().addClass('disabled');
    }




//layeers part -------------------------

   



    $(selectors.scaleX).click(function () {
        scale = -scale;
        $image.cropper("scaleX", scale);
        if($(this).is("a")) return false;
    });

    function updateFit($fitBox){
        if($fitBox.prop('checked')){
            $('.img').append($('<div class="fit-overlay"></div>'));
            $('.img').addClass('fitted');
            let cropBoxData = $image.cropper('getData');
            let imageData = $image.cropper('getImageData');
            if(!vertical){
                cropBoxData.y = imageData.naturalHeight / 2 - cropBoxData.height / 2;
                $(selectors.image).cropper('setData', cropBoxData);
                let ratio = cropBoxData.height / imageData.naturalHeight;
                $(selectors.image).cropper("scale", 1, ratio);
            }else{
                cropBoxData.x = imageData.naturalWidth / 2 - cropBoxData.width / 2;
                $(selectors.image).cropper('setData', cropBoxData);
                let ratio = cropBoxData.width / imageData.naturalWidth;
                $(selectors.image).cropper("scale", ratio, 1);
            }
        }else{
            $('.img').removeClass('fitted');
            $(selectors.image).cropper("scale", 1, 1);
            $('.img .fit-overlay').remove();
        }
    }

    $(selectors.fitCropper).change(function () {
        updateFit($(this));
    });

    function cropToArea($cropCheckbox){
        let url;
        if($cropCheckbox.prop('checked')) {
            originalUrl = $image.attr('src');
            let imageBase64 = $image.cropper('getCroppedCanvas').toDataURL();
            url = imageBase64;
        }else{
            url = originalUrl;
        }
        $image.cropper('replace', url).ready(function(){
            setTimeout(function(){
                $(selectors.image).cropper("clear");
                updateCropperSizes();
                }, 100);
        });
    }

    $(selectors.cropToArea).change(function () {
        cropToArea($(this));
    });

    $(selectors.onOff).change(function () {
    	if(!$(this).prop('checked')){
    		$(selectors.image).cropper("clear");
    	}
    	else {
    		$(selectors.dataWidth).trigger("keyup");
    		
    	}
        if($(this).is("a")) return false;
    });


    $(selectors.offEffects).click(function () {
    	
    	
    	
        blackWhite = false;
        sepia = false;
        //currentFilter = '';
        scale = -1;
        $(selectors.scaleX).trigger("click");
        addLayer();
        if($(this).is("a")) return false;
    });

    $(selectors.addGrayScale).click(function () {
        blackWhite = !blackWhite;
        sepia = false;
        addLayer();
        if($(this).is("a")) return false;
    });

    $(selectors.sepia).click(function () {
        sepia = !sepia;
        blackWhite = false;
        addLayer();
        if($(this).is("a")) return false;
    });



    $(selectors.dataWidth + "," + selectors.dataHeight).keyup(function () {
        updateCropperSizes();
    });

    function updateCropperSizes() {
        var width = $(selectors.dataWidth).val();
        var height = $(selectors.dataHeight).val();
        if (isNaN(width) || width < 1 || isNaN(height) || height < 1) {
            return;
        }

        if (!$(selectors.onOff).prop('checked')) return;

        var cropBoxData = $image.cropper('getData');
        var getImageData = $image.cropper('getImageData');
        console.log(cropBoxData, getImageData);

        var oW = parseFloat(getImageData.naturalWidth);
        var oH = parseFloat(getImageData.naturalHeight);

        var pW = parseFloat($(selectors.dataWidth).val());
        var pH = parseFloat($(selectors.dataHeight).val());

        if (pH > heightProportion) {
            pH = heightProportion;
            $(selectors.dataHeight).val(pH);
        }

        var bigW = Math.round(oW / (oH / heightProportion));
        if (pW > bigW) {
            pW = bigW;
            $(selectors.dataWidth).val(bigW);
        }

        var nW, nH;

        if (pW > pH) {
            nW = oW;
            cmPixelSize = oW / pW;
            nH = cmPixelSize * pH;
            console.log("MAx >>> 1");


        } else if (pW < pH) {
            nH = oH;
            cmPixelSize = oH / pH;

            nW = cmPixelSize * pW;
            console.log("MAx >>> 2");


        } else if (pW == pH) {

            if (oW > oH) {
                cmPixelSize = oH / pH;
                nH = oH;
                nW = oH;

            } else if (oW <= oH) {
                cmPixelSize = oW / pW;
                nH = oW;
                nW = oW;

            }
        }
        var szBl = fullBleed(oW, oH, nW, nH);

        nW = Math.round(szBl.width);
        nH = Math.round(szBl.height);

        showLeftRight(false);
        showTopBottom(false);

        if (nW == oW) {
            vertical = false;
            showTopBottom(true);
        }

        if (nH == oH) {
            vertical = true;
            showLeftRight(true);
        }


        console.log("New W New H" + nW + ">>>" + nH);

        cropBoxData.width = Math.round(nW);
        cropBoxData.height = Math.round(nH);
        $image.cropper('crop');
        $image.cropper('setData', cropBoxData);
        updateFit($(selectors.fitCropper));
    }


    function addLayer() {

        var images = [
        	$image.attr('src'),
        ];
        if (currentFilter)
            images.push(currentFilter);

        $("#canvas").canvasLayout({
            'grayScale': blackWhite,
            'sepia': sepia,
            'img': images, //  [$('#image').attr('src'), 'img/SpongeBob_and_Patrick_-_Transparent_-_Low_Opacity.png'],
            'onComplete': function (dataUrl) {
                //$image.cropper('reset');
                //$image.cropper('replace',dataUrl);
                $('.cropper-canvas img').attr('src', dataUrl);
                $('.cropper-view-box img').attr('src', dataUrl);
            }
        });


    }

    $(selectors.addLayout).click(function () {
        if (currentFilter !== $(this).attr("data-img")) {
            currentFilter = $(this).attr("data-img");
        } else {
            currentFilter = "";
        }

        addLayer();
        if($(this).is("a")) return false;
    });





});