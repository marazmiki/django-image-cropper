from django.db import settings
from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template as render
from django.utils import simplejson
from django.http import HttpResponse
 
def upload_success(request, form, original):
    """
    Default success upload handler
    """
    return redirect(original)

def crop_success(request, form, original, cropped):
    """
    Default success crop handler
    """
    if request.is_ajax():
        return HttpResponse(
            simplejson.dumps({
                'image': {
                    'url': cropped.image.url,
                    'width': cropped.w,
                    'height': cropped.h,
                }   
            }),
            mimetype='application/x-json',
        ) 

    return render(request, 'cropper/crop.html', {
        'form'     : form,
        'cropped'  : cropped,
        'original' : original,
    })
    
    return redirect(original)