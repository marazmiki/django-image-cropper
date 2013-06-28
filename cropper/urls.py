from django.conf.urls import url
from cropper.views import UploadView, CropView

urlpatterns = [
    url('^$', UploadView.as_view(), name='cropper_upload'),
    url('^(?P<original_id>\d+)/$', CropView.as_view(),   name='cropper_crop'),
]
