$(function ()
{

    $('#grid_compare_hl').find('.grid-item').draggable({
        revert: 'invalid', helper: 'clone'
    });

    $('#grid_compare_normal').find('.grid-item').draggable({
        revert: 'invalid', helper: 'clone'
    });


    $('#grid_compare_drop').find('.grid-item').droppable({
        drop: function (event, ui)
        {
            $(window).trigger('atm-comparador-agregar',{
            'equipo_marca': ui.draggable[0].dataset.itemBrand,
            'equipo_modelo': ui.draggable[0].dataset.itemBrand + " " + ui.draggable[0].dataset.itemModel,
            'equipo_so': ui.draggable[0].dataset.itemOs,
            'tipo_de_agregado': 'Drag & Drop' });

            $(this).removeClass('grid-item-open');
            $(this).html('<p style="margin: 0; padding: 5px 0 0; text-align: center;"><img src="' + $(ui.draggable).attr('data-image-url') + '" width="39" height="71" /></p><p>' + $(ui.draggable).attr('data-item-brand') + ' <br />' + $(ui.draggable).attr('data-item-model') + '</p><span class="grid-item-close" data-item-id="' + $(ui.draggable).attr('data-item-id') + '"></span>');
            
            switch ($(this).index())
            {
                case 0:
                    $('#grid_compare_drop').find('input[name="hidEquipo1"]').val($(ui.draggable).attr('data-item-id').substr($(ui.draggable).attr('data-item-id').indexOf('_') + 1));
                    //_gaq.push(['_trackEvent', 'Smartphones Comparar', 'Drag-n-drop', '1']);
                    break;
                case 1:
                    $('#grid_compare_drop').find('input[name="hidEquipo2"]').val($(ui.draggable).attr('data-item-id').substr($(ui.draggable).attr('data-item-id').indexOf('_') + 1));
                    //_gaq.push(['_trackEvent', 'Smartphones Comparar', 'Drag-n-drop', '2']);
                    break;
                case 2:
                    $('#grid_compare_drop').find('input[name="hidEquipo3"]').val($(ui.draggable).attr('data-item-id').substr($(ui.draggable).attr('data-item-id').indexOf('_') + 1));
                    //_gaq.push(['_trackEvent', 'Smartphones Comparar', 'Drag-n-drop', '3']);
                    break;
                case 3:
                    $('#grid_compare_drop').find('input[name="hidEquipo4"]').val($(ui.draggable).attr('data-item-id').substr($(ui.draggable).attr('data-item-id').indexOf('_') + 1));
                    //_gaq.push(['_trackEvent', 'Smartphones Comparar', 'Drag-n-drop', '4']);
                    break;
            }

            // set checked and disabled checkbox
            //$(ui.draggable).find('.grid-option-compare-check').attr({ 'checked': 'checked', 'disabled': 'disabled' });
            $(ui.draggable).find('.grid-option-compare-check').attr({ 'checked': 'checked' });

            //disable draggable item
            $(ui.draggable).draggable('disable');

            //set close button
            $(this).find('.grid-item-close').bind('click', mozz_cleanDroppedItem);

            $(this).droppable({ disabled: true });

            $('#grid_compare_drop').find('.grid-item-open').length <= 2 ? $('.link-compare').show() : $('.link-compare').hide();
        }
    });

    $('#grid_compare_hl').find('.grid-item').find('.grid-option-compare-check').bind('click', mozz_setDroppedItem);
    $('#grid_compare_normal').find('.grid-item').find('.grid-option-compare-check').bind('click', mozz_setDroppedItem);

});



function mozz_cleanDroppedItem()
{
        var indexPos = $(this).parent().attr('index-pos');
        $('.grid-item[data-item-id="' + $(this).attr('data-item-id') + '"]').draggable('enable');
        $('.grid-item[data-item-id="' + $(this).attr('data-item-id') + '"]').find('.grid-option-compare-check').removeAttr('checked');
        $('.grid-item[data-item-id="' + $(this).attr('data-item-id') + '"]').find('.grid-option-compare-check').removeAttr('disabled');
        $(this).parent().addClass('grid-item-open');
        $(this).parent().droppable({ disabled: false });
        $(this).parent().html('');

        $(window).trigger('atm-comparador-quitar',{
                'equipo_marca': $('.grid-item[data-item-id="' + $(this).attr('data-item-id') + '"]')[0].dataset.itemBrand,
                'equipo_modelo': $('.grid-item[data-item-id="' + $(this).attr('data-item-id') + '"]')[0].dataset.itemBrand + " " + $('.grid-item[data-item-id="' + $(this).attr('data-item-id') + '"]')[0].dataset.itemModel,
                'equipo_so': $('.grid-item[data-item-id="' + $(this).attr('data-item-id') + '"]')[0].dataset.itemOs});

        $(window).trigger('atm-comparador-agregar',
    {
        'equipo_id': '$id',
        'equipo_marca': '$marca',
        'equipo_modelo': '$modelo',
        'equipo_so': '$sistema-operativo'
    }
    );
        
        switch (eval(indexPos))
        {
            case 0:

                $('#grid_compare_drop').find('input[name="hidEquipo1"]').val(0);
                _gaq.push(['_trackEvent', 'Smartphones Comparar', 'Quitar']);
                break;
            case 1:
                $('#grid_compare_drop').find('input[name="hidEquipo2"]').val(0);
                _gaq.push(['_trackEvent', 'Smartphones Comparar', 'Quitar']);
                break;
            case 2:
                $('#grid_compare_drop').find('input[name="hidEquipo3"]').val(0);
                _gaq.push(['_trackEvent', 'Smartphones Comparar', 'Quitar']);
                break;
            case 3:
                $('#grid_compare_drop').find('input[name="hidEquipo4"]').val(0);
                _gaq.push(['_trackEvent', 'Smartphones Comparar', 'Quitar']);
                break;
        }

        $('#grid_compare_drop').find('.grid-item-open').length <= 2 ? $('.link-compare').show() : $('.link-compare').hide();
}



function mozz_setDroppedItem() 
{
    var itemGrid = $(this).parent().parent().parent();

    var unlock;

    var itemFound = false;

    for (i = 0; i < 4; i++)
    {
        div=$('#grid_compare_drop').find('.grid-item')[i];
        //alert($(div).find('span').attr('data-item-id'));
        if ($(div).find('span').attr('data-item-id') == itemGrid.attr('data-item-id'))
        {
            unlock = div;
            itemFound = true;
            //alert(1);
        }
    }

    if (!itemFound)
    {
        if ($('#grid_compare_drop').find('.grid-item-open').length > 0)
        {

            $(window).trigger('atm-comparador-agregar',{
            'equipo_marca': itemGrid.attr('data-item-brand'),
            'equipo_modelo': itemGrid.attr('data-item-brand') + " " + itemGrid.attr('data-item-model'),
            'equipo_so': itemGrid.attr('data-item-os'),
            'tipo_de_agregado': 'Checkbox' });

            switch ($('#grid_compare_drop').find('.grid-item-open:eq(0)').index())
            {
                case 0:
                    $('#grid_compare_drop').find('input[name="hidEquipo1"]').val(itemGrid.attr('data-item-id').substr(itemGrid.attr('data-item-id').indexOf('_') + 1));
                    break;
                case 1:
                    $('#grid_compare_drop').find('input[name="hidEquipo2"]').val(itemGrid.attr('data-item-id').substr(itemGrid.attr('data-item-id').indexOf('_') + 1));
                    break;
                case 2:
                    $('#grid_compare_drop').find('input[name="hidEquipo3"]').val(itemGrid.attr('data-item-id').substr(itemGrid.attr('data-item-id').indexOf('_') + 1));
                    break;
                case 3:
                    $('#grid_compare_drop').find('input[name="hidEquipo4"]').val(itemGrid.attr('data-item-id').substr(itemGrid.attr('data-item-id').indexOf('_') + 1));
                    break;
            }
            $('#grid_compare_drop').find('.grid-item-open:eq(0)').droppable({ disabled: true });
            $('#grid_compare_drop').find('.grid-item-open:eq(0)').html('<p style="margin: 0; padding: 5px 0 0; text-align: center;"><img src="' + $(itemGrid).attr('data-image-url') + '" width="39" height="71" /></p><p>' + $(itemGrid).attr('data-item-brand') + ' <br />' + $(itemGrid).attr('data-item-model') + '</p><span class="grid-item-close" data-item-id="' + $(itemGrid).attr('data-item-id') + '"></span>');
            $('#grid_compare_drop').find('.grid-item-open:eq(0)').find('.grid-item-close').bind('click', mozz_cleanDroppedItem);
            $('#grid_compare_drop').find('.grid-item-open:eq(0)').removeClass('grid-item-open');

            $(itemGrid).draggable('disable');

            //$(this).attr({ 'checked': 'checked', 'disabled': 'disabled' });
            $(this).attr({ 'checked': 'checked' });
            //_gaq.push(['_trackEvent', 'Smartphones Comparar', 'Anadir']);
        }
        else
        {
            return false;
        }
    }
    else
    {
        var indexPos = $(unlock).attr('index-pos');

        $(itemGrid).draggable('enable');
        $(itemGrid).find('.grid-option-compare-check').removeAttr('checked');
        $(itemGrid).find('.grid-option-compare-check').removeAttr('disabled');
        $(unlock).addClass('grid-item-open');
        $(unlock).droppable({ disabled: false });
        $(unlock).html('');

        switch (eval(indexPos))
        {
            case 0:
                $('#grid_compare_drop').find('input[name="hidEquipo1"]').val(0);
                break;
            case 1:
                $('#grid_compare_drop').find('input[name="hidEquipo2"]').val(0);
                break;
            case 2:
                $('#grid_compare_drop').find('input[name="hidEquipo3"]').val(0);
                break;
            case 3:
                $('#grid_compare_drop').find('input[name="hidEquipo4"]').val(0);
                break;
        }
    }

    $('#grid_compare_drop').find('.grid-item-open').length <= 2 ? $('.link-compare').show() : $('.link-compare').hide();

}

