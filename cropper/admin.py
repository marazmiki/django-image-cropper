from django.contrib import admin
from django.shortcuts import get_object_or_404, render_to_response
from django.conf.urls.defaults import patterns, url
from django.conf import settings
from cropper.models import Original, Cropped
from cropper import settings as cropper_settings

class OriginalAdmin(admin.ModelAdmin):
    ''

admin.site.register(Original, OriginalAdmin)


class CroppedAdmin(admin.ModelAdmin):
    ''
    
    def admin_cropper_crop(self, request, original_id=None):
        original = get_object_or_404(Original, id=original_id)
        return render_to_response("admin/cropper/cropped/crop.html", {'original': original, 'MEDIA_URL': settings.MEDIA_URL, 'ALLOWED_DIMENSIONS': cropper_settings.ALLOWED_DIMENSIONS})

    def get_urls(self):
        urls = super(CroppedAdmin, self).get_urls()
        my_urls = patterns('',
            url(
                r'crop_image/((?P<original_id>\d+)/)?$',
                self.admin_site.admin_view(self.admin_cropper_crop),
                name='admin_cropper_crop',
            ),
        )
        return my_urls + urls

admin.site.register(Cropped, CroppedAdmin)