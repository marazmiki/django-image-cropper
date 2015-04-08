# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.contrib import admin
from cropper.models import Original, Cropped
from cropper import settings


class OriginalAdmin(admin.ModelAdmin):
    """
    Admin class for original image model
    """


class CroppedAdmin(admin.ModelAdmin):
    """
    Admin class for cropped image model
    """


if settings.SHOW_ADMIN:
    admin.site.register(Original, OriginalAdmin)
    admin.site.register(Cropped, CroppedAdmin)
