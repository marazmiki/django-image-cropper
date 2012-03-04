from django.conf.urls.defaults import patterns, url
from cropper.views import UploadView, CropView

urlpatterns = patterns('',
    url('^$',                       UploadView.as_view(), name='cropper_upload'),
    url('^(?P<original_id>\d+)/$',  CropView.as_view(),   name='cropper_crop'),
)
