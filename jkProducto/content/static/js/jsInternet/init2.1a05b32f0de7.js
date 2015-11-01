//set scrollstart & scrollend events
$(function () {


    var urlType =  location.href;
    var cboType = urlType.split('../index.html');

    if(cboType[3] == 'smartphones'){
        $('.form-dropdown-type span').text('Smartphones')
    }else if(cboType[3] == 'basicos'){
        $('.form-dropdown-type span').text('Básicos')
    }


    var special = jQuery.event.special,
        uid1 = 'D' + (+new Date()),
        uid2 = 'D' + (+new Date() + 1);
        
    special.scrollstart = {
        setup: function () {

            var timer,
                handler = function (evt) {

                    var _self = this,
                        _args = arguments;

                    if (timer) {
                        clearTimeout(timer);
                    } else {
                        evt.type = 'scrollstart';
                        jQuery.event.handle.apply(_self, _args);
                    }

                    timer = setTimeout(function () {
                        timer = null;
                    }, special.scrollstop.latency);

                };

            $(this).bind('scroll', handler).data(uid1, handler);

        },
        teardown: function () {
            $(this).unbind('scroll', $(this).data(uid1));
        }
    };
    
    special.scrollstop = {
        latency: 300,
        setup: function () {

            var timer,
                handler = function (evt) {

                    var _self = this,
                        _args = arguments;

                    if (timer) {
                        clearTimeout(timer);
                    }

                    timer = setTimeout(function () {

                        timer = null;
                        evt.type = 'scrollstop';
                        jQuery.event.handle.apply(_self, _args);

                    }, special.scrollstop.latency);

                };

            $(this).bind('scroll', handler).data(uid2, handler);

        },
        teardown: function () {
            $(this).unbind('scroll', $(this).data(uid2));
        }
    };

    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('.scrollup').fadeIn();
        } else {
            $('.scrollup').fadeOut();
        }
    });

    $('.scrollup').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });




});

$(function () {


    $('#promotion-ss .close').click(function () {
        $(this).parent().delay(200).animate({
            bottom: -300
        });
    });


    mozz_detectSyncResources();
    // set async elements
    var array_async_photo = $('.async-photo');

    for (var i = 0; i < array_async_photo.length; i++) {
        async_photo_offset = $(array_async_photo[i]).offset();
        if (async_photo_offset.top > $(window).scrollTop() && async_photo_offset.top < $(window).scrollTop() + $(window).height()) {
            mozz_loadResourceAsync(array_async_photo[i]);
        }
    }

    $(window).bind('scrollstop', mozz_detectSyncResources);

    //cookieLayer(1); // quitar ligthbox 01/102014

    //cookieLayerNokia(1);
    //play();
    //playNokiaUno();
    //cookieLayerNokia(5);

    //replaceBody('<object type="application/x-shockwave-flash"  data="../swf/1227x753.swf" width="1227" height="753"><param name="movie" value="../swf/1227x753.swf" /><param name="quality" value="high" /><param name="bgcolor" value="#999999" /><param name="play" value="true" /><param name="loop" value="true" /><param name="wmode" value="transparent" /><param name="scale" value="showall" /><param name="menu" value="true" /><param name="devicefont" value="false" /><param name="salign" value="" /><param name="allowScriptAccess" value="always" /><!--[if !IE]>--><object name="gamecast" type="application/x-shockwave-flash" data="../swf/1227x753.swf"  width="1227" height="753"><param name="movie" value="../swf/1227x753.swf" /><param name="quality" value="high" /><param name="bgcolor" value="#999999" /><param name="play" value="true" /><param name="loop" value="true" /><param name="wmode" value="transparent" /><param name="scale" value="showall" /><param name="menu" value="true" /><param name="devicefont" value="false" /><param name="salign" value="" /><param name="allowScriptAccess" value="always" /><!--<![endif]--><a href="http://www.adobe.com/go/getflash"><img src="http://www.adobe.com/images/shared/download_buttons/get_flash_player.gif" alt="Obtener Adobe Flash Player" /></a><!--[if !IE]>--></object><!--<![endif]--></object>');
    //replaceBody('');
    fixComparador();
});

function fixComparador() {
    var hidden1 = $('#hidEquipo1').val();
    var hidden2 = $('#hidEquipo2').val();
    var hidden3 = $('#hidEquipo3').val();
    var hidden4 = $('#hidEquipo4').val();
    if (hidden1 != '0') {
        $('#hidEquipo1').val('0');
    }
    if (hidden2 != '0') {
        $('#hidEquipo2').val('0');
    }
    if (hidden3 != '0') {
        $('#hidEquipo3').val('0');
    }
    if (hidden4 != '0') {
        $('#hidEquipo4').val('0');
    }
}














