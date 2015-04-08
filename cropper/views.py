# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import FormView
from cropper.models import Original
from cropper.forms import CroppedForm, OriginalForm
from cropper.compat import JsonResponse


class UploadView(FormView):
    """
    Upload picture to future cropping
    """
    form_class = OriginalForm
    template_name = 'cropper/upload.html'

    def success(self, request, form, original):
        return redirect(original)

    def form_valid(self, form):
        original = form.save()
        return self.success(self.request, form, original)


class CropView(FormView):
    """
    Crop picture and save result into model
    """
    form_class = CroppedForm
    template_name = 'cropper/crop.html'

    def get_object(self):
        """
        Returns the original image object
        """
        return get_object_or_404(Original, pk=self.kwargs['original_id'])

    def get_initial(self):
        """
        Initial dictionary that passed into form instance arguments
        """
        return {'original': self.get_object()}

    def get_context_data(self, **kwargs):
        """
        Context dictionary that passed into template renderer
        """
        return {
            'form': self.get_form(self.form_class),
            'original': self.get_object(),
            'cropped': None
        }

    def form_valid(self, form):
        cropped = form.save(commit=False)
        cropped.save()

        if self.request.is_ajax():
            return JsonResponse({
                'image': {
                    'url': cropped.image.url,
                    'width': cropped.w,
                    'height': cropped.h,
                }})
        return render(self.request, 'cropper/crop.html', {
            'form': form,
            'cropped': cropped,
            'original': self.get_object()
        })
