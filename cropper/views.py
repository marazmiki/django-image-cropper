from django.views.generic.simple import direct_to_template as render
from django.shortcuts import get_object_or_404
from cropper import settings
from cropper.forms import CroppedForm, OriginalForm
from cropper.models import Original

def upload(request, form_class=OriginalForm,
           success=settings.UPLOAD_SUCCESS,
           template_name='cropper/upload.html' 
    ):
    """
    Upload picture to future cropping
    """
    form = form_class(request.POST or None, request.FILES or None)

    if form.is_valid():
        original = form.save()
        return success(request, form, original)

    return render(request, template_name, {
        'form': form,
    })

def crop(request, original_id, form_class=CroppedForm,
         success=settings.CROP_SUCCESS
    ):
    """
    Crop picture and save result into model
    """
    original = get_object_or_404(Original, pk=original_id)
    cropped = None

    form = form_class(request.POST or None, initial={'original': original})

    if form.is_valid():
        cropped = form.save(commit=False)
        cropped.save()
        return success(request, form, original, cropped)

    return render(request, 'cropper/crop.html', {
        'form'     : form,
        'cropped'  : cropped,
        'original' : original,
    })