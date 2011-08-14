(function($){
    var cropbox = $('#cropbox'),
        preview = $('#preview'),
        cropboxHeight = cropbox.height(),
        cropboxWidth  = cropbox.width(),
        previewHeight = preview.closest('DIV').height(),
        previewWidth  = preview.closest('DIV').width()
    ;

    var showPreview = function(coords)
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
    };

    $(function(){
        cropbox.Jcrop({
            onChange: showPreview,
            onSelect: showPreview,
            bgColor   : '#cccccc',
            bgOpacity : 0.8

         //   aspectRatio: 1
        });

        $('#crop-form').submit(function(){
            $.post(
                $(this).attr('action'),
                $(this).serialize(),
                function(json){
                
                }, 'json'
            );
            return false;
        });
    });


})(jQuery);


/*
(function($){
    $(function(){        
        var target = $('#image-original');
        var cropForm = $('#crop-form');
        var cropPreview = $('#crop-preview');        
        var showCoords = function(c){
            $(['x', 'y', 'w', 'h']).each(function(){
                $('#id_' + this).val(c[this]);
            });
        };   
        target.Jcrop({
            addClass    : 'custom',    
            bgColor     : '#cccccc',
            bgOpacity   : 0.8,
            onSelect    : showCoords,
            onChange    : showCoords,
            sideHandles : true,
            allowSelect : true,
            allowMove   : true,
            allowResize : true,
            dummy: null
        });
        cropForm.submit(function(){
            cropPreview.html('');
            $.post(
                $(this).attr('action'),
                $(this).serialize(),
                function(json){
                    preview = $('img');
                    preview.width(json.image.width);
                    preview.height(json.image.height);
                    preview.attr('src', json.image.url);

                    cropPreview.append(preview)
                }, 'json'
            );
            return false;
        });
    });
})(window.jQuery);
*/