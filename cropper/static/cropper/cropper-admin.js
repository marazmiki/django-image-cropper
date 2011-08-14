(function($){
    var cropbox = $('#cropbox'),
        preview = $('#preview'),
        cropboxHeight = cropbox.height(),
        cropboxWidth  = cropbox.width(),
        previewHeight = preview.closest('DIV').height(),
        previewWidth  = preview.closest('DIV').width(),
        saveCrop = $('#save_crop'),
        cancelCrop = $('#cancel_crop'),
        clearCrop = $('#clear_crop'),
        id_original = $('#id_original'),
        id_x = $('#id_x'),
        id_y = $('#id_y'),
        id_w = $('#id_w'),
        id_h = $('#id_h'),
        id_w_d = $('#id_w_display'),
        id_h_d = $('#id_h_display'),
        showPreview = function(coords)
        {
            $(['x', 'y', 'w', 'h']).each(function(){
                $('#id_' + this).val(coords[this]);
            });

            if (parseInt(coords.w) > 0)
            {
                var rx = previewWidth  / coords.w;
                var ry = previewHeight / coords.h;

                preview.css({
                    width  : Math.round(rx * cropboxWidth  ) + 'px',
                    height : Math.round(ry * cropboxHeight ) + 'px',
                    marginLeft : '-' + Math.round(rx * coords.x) + 'px',
                    marginTop  : '-' + Math.round(ry * coords.y) + 'px'
                });
            };
        },
        cbox_options = {
          onChange: showPreview,
          onSelect: showPreview,
          bgColor   : '#cccccc',
          bgOpacity : 0.8,
          boxWidth: 600,
          boxHeight: 600
        },
        api,
        currentCrop = $('option:selected', id_original).data('cropper-coords'),
        aspectRatio = $('#dim_restrictions option:selected').data('aspectRatio'),
        minSize = $('#dim_restrictions option:selected').data('minSize');
        
    if(currentCrop && currentCrop.x && currentCrop.y && currentCrop.w && currentCrop.h)
    {
      cbox_options.setSelect = [parseInt(currentCrop.x, 10), parseInt(currentCrop.y, 10), parseInt((currentCrop.x*1 + currentCrop.w*1), 10),  parseInt((currentCrop.y*1 + currentCrop.h*1), 10)];
    }
    if(aspectRatio)
    {
      cbox_options.aspectRatio = aspectRatio;
    }
    if(minSize)
    {
      cbox_options.minSize = minSize;
      $('#crop-mask').css({'width': minSize[0]+'px', 'height': minSize[1]+'px'});
    }
    
    api = $.Jcrop(cropbox, cbox_options);
    
    
    if($('#dim_restrictions').length == 1)
    {
      $('#dim_restrictions').change(function(){
        var newSize = $('option:selected', this).data('minSize'),
            newRatio = $('option:selected', this).data('aspectRatio');
        if(newSize)
        {
          cbox_options.minSize = newSize;
          cbox_options.setSelect = [0, 0, newSize[0], newSize[1]];
          $('#crop-mask').css({'width': newSize[0]+'px', 'height': newSize[1]+'px'});
          previewWidth = newSize[0];
          previewHeight = newSize[1];
          id_w_d.val(newSize[0]);
          id_h_d.val(newSize[1]);
        }
        if(newRatio)
        {
          cbox_options.aspectRatio = newRatio;
        }
        api.destroy();
        api = $.Jcrop(cropbox, cbox_options);
      }).change();
    }
    
    saveCrop.click(function(e){
      e.preventDefault();
      e.stopPropagation();
      $('option:selected', id_original).data('cropper-coords', {x: id_x.val(), y: id_y.val(), w: id_w.val(), h: id_h.val(), w_d: id_w_d.val(), h_d: id_h_d.val()});
      $('.jqmWindow').jqmHide();
    });
    
    cancelCrop.click(function(e){
      e.preventDefault();
      e.stopPropagation();
      var storedData = $('option:selected', id_original).data('cropper-coords'),
          newData = storedData ? storedData : {x: 0, y: 0, w: '', h: '', id_w_d: '', id_h_d: ''};
      id_x.val(newData.x);
      id_y.val(newData.y);
      id_w.val(newData.w);
      id_h.val(newData.h);
      id_w_d.val(newData.w_d);
      id_h_d.val(newData.h_d);
      $('.jqmWindow').jqmHide();
    });
    
    clearCrop.click(function(e){
      e.preventDefault();
      e.stopPropagation();
      api.release();
      id_x.val(0);
      id_y.val(0);
      id_w.val('');
      id_h.val('');
      id_w_d.val('');
      id_h_d.val('');
    });
    


})(jQuery);

