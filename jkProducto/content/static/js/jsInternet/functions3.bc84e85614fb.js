function mozz_setInfo(event) {

    overlayOptions = typeof event.data !== 'undefined' ? event.data : false;

    var strYTBlock = '<div class="block" style="padding: 10px;"><iframe allowtransparency="true" class="video-canvas" style="background-color: #000; margin: 0 auto; display: block;" width="880" height="380" src="' + overlayOptions.overlayUrl + '" frameborder="0" allowfullscreen></iframe></div>'

    $('body').append('<div class="overlay" id="overlay_bg"></div><div id="overlay_block" class="overlay-block"><div class="overlay-block-title">' + overlayOptions.overlayTitle + '<span class="overlay-close"></span></div><div class="overlay-block-content">' + strYTBlock + '</div></div>')
    $('#overlay_block').find('.overlay-close').bind('click', function () {
        $('#overlay_bg').remove();
        $('#overlay_block').remove();
    });

}



//Tag Priority
function mozz_setPriority(e) {
    _gaq.push(['_trackEvent', 'banner-catalogo', 'priority', 'boton']);
}

function mozz_detectSyncResources()
{

    // set async elements
    var array_async_element = $('.async-photo');

    for(var i = 0; i < array_async_element.length; i++)
    {
        async_element_offset = $(array_async_element[i]).offset();
        async_element = $(array_async_element[i]);
        if(async_element_offset.top >= $(window).scrollTop() && async_element_offset.top < $(window).scrollTop() + $(window).height() && async_element.find('async-photo').length == 0 && async_element.find('async-photo').length == 0 )
        {
            mozz_loadResourceAsync( async_element );
        }
    }

}


function mozz_detectSyncResourcesInit() {
    // set async elements
    var array_async_element = $('.async-photo');

    for (var i = 0; i < array_async_element.length; i++) {
        async_element_offset = $(array_async_element[i]).offset();
        async_element = $(array_async_element[i]);

        mozz_loadResourceAsync(async_element);


    }

}


function mozz_loadResourceAsync(asyncElement) {

    multimediaCanvas = jQuery(asyncElement).children('.multimedia-canvas');
    jQuery(asyncElement).removeClass('async-photo');

    jQuery(multimediaCanvas).children('.image-canvas').addClass('decoration-loading');

    jQuery(multimediaCanvas).children('.image-canvas').append(jQuery('<img style="display:none;" />').attr({
        'src': jQuery.support.leadingWhitespace ? jQuery(asyncElement).attr('data-image-url') : jQuery(asyncElement).attr('data-image-url') + '?timestamp=' + new Date().getTime(),
        'width': jQuery(asyncElement).attr('data-image-width'),
        'height': jQuery(asyncElement).attr('data-image-height')
    }));
    jQuery(multimediaCanvas).children('.image-canvas').children('img').load(function () {
        jQuery(this).parent().removeClass('decoration-loading');
        jQuery(this).fadeIn('fast');
    }).error(function () {
        jQuery(this).parent().parent().addClass('async-photo');
    })

}

function mozz_setCoverflow(sliderBlock)
{
    sliderThumbBlock = $('#' + sliderBlock).find('.coverflow-block')
    sliderThumbList = $(sliderThumbBlock).children('.coverflow-list')

    /* set thumb canvas width */
    $(sliderThumbList).width($(sliderThumbList).children('.coverflow-item').length * $(sliderThumbList).children('.coverflow-item').outerWidth(true))
    /* set thumb block height */
    $(sliderThumbBlock).height($(sliderThumbList).children('.coverflow-item').outerHeight(true))

    widthThumbBlock = $(sliderThumbBlock).width()
    widthThumbList = $(sliderThumbList).width()

    /* attach click event to thumbnails */
    $(sliderThumbList).children('.coverflow-item').bind('click', function (e, continueAnimation) {

        continueAnimation = typeof continueAnimation !== 'undefined' ? continueAnimation : false;

        thumbIndex = $(this).parent().children('.coverflow-item').index(this)

        heightThumbItem = $(sliderThumbList).children('.coverflow-item:eq(' + thumbIndex + ')').outerHeight(true)
        widthThumbItem = $(sliderThumbList).children('.coverflow-item:eq(' + thumbIndex + ')').outerWidth(true)

        centerThumbList = widthThumbBlock / 2 - widthThumbItem / 2

        $(this).parent().children('.coverflow-item').removeClass('coverflow-item-selected')
        $(this).addClass('coverflow-item-selected');

        leftThumbList = centerThumbList - $(this).position().left;
        $(this).parent().animate({ 'left': leftThumbList }, widthThumbBlock);

    });

    $('#' + sliderBlock).find('.coverflow-nav').bind('click', function () {
        $(this).hasClass('coverflow-nav-prev') ? $(sliderThumbList).find('.coverflow-item-selected').prev().trigger('click') : $(sliderThumbList).find('.coverflow-item-selected').next().trigger('click');
    });
}


function mozz_setCoverflowCompare(sliderBlock)
{
    sliderThumbBlock = $('#' + sliderBlock).find('.coverflow-block')
    sliderThumbList = $(sliderThumbBlock).children('.coverflow-list')

    /* set thumb canvas width */
    $(sliderThumbList).width($(sliderThumbList).children('.coverflow-item').length * $(sliderThumbList).children('.coverflow-item').outerWidth(true))
    /* set thumb block height */
    $(sliderThumbBlock).height($(sliderThumbList).children('.coverflow-item').outerHeight(true))

    widthThumbBlock = $(sliderThumbBlock).width()
    widthThumbList = $(sliderThumbList).width()

    /* attach click event to thumbnails */
    $(sliderThumbList).children('.coverflow-item').bind('click', function (e, continueAnimation)
    {

        continueAnimation = typeof continueAnimation !== 'undefined' ? continueAnimation : false;

        thumbIndex = $(this).parent().children('.coverflow-item').index(this)

        heightThumbItem = $(sliderThumbList).children('.coverflow-item:eq(' + thumbIndex + ')').outerHeight(true)
        widthThumbItem = $(sliderThumbList).children('.coverflow-item:eq(' + thumbIndex + ')').outerWidth(true)

        centerThumbList = widthThumbBlock / 2 - widthThumbItem / 2

        $(this).parent().children('.coverflow-item').removeClass('coverflow-item-selected')
        $(this).addClass('coverflow-item-selected');

        leftThumbList = centerThumbList - $(this).position().left;
        $(this).parent().animate({ 'left': leftThumbList }, widthThumbBlock);
        //***DRAG
        $('#coverflow_smart').find('.coverflow-item-selected').draggable({
            revert: 'invalid', helper: 'clone', appendTo: '.wrapper'
        });


        //***
    });

    $('#' + sliderBlock).find('.coverflow-nav').bind('click', function ()
    {
        $(this).hasClass('coverflow-nav-prev') ? $(sliderThumbList).find('.coverflow-item-selected').prev().trigger('click') : $(sliderThumbList).find('.coverflow-item-selected').next().trigger('click');
    });
}

function mozz_setPhoneFilter(e) {
    e.type == 'click' ? $(this).find('.form-dropdown-list').show() : $(this).find('.form-dropdown-list').hide();

}



function isCheck4g() {
    sHash = window.location.hash.toLowerCase()
    if (sHash === "#4g") {
        $('#checkRenueva').attr('checked',true);
        busRenu();
    }
}


