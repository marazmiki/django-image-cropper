from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cropper.views',
    url('^$', view='upload', name='cropper_upload'),
    url('^(?P<original_id>\d+)/$', view='crop', name='cropper_crop'),
)
