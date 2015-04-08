# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.conf.urls import url
from cropper.views import UploadView, CropView


urlpatterns = [
    url('^$', UploadView.as_view(), name='cropper_upload'),
    url('^(?P<original_id>\d+)/$', CropView.as_view(), name='cropper_crop')
]
