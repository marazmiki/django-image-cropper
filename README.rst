====================
django-image-cropper
====================

This application used for image cropping. User can upload image or photo,
pick wished area up and save image. 

The license is MIT.

Installation
============
First of all, plese install django-image-cropper:

::

    pip install django-image-cropper

Then you must edit your settings module: add item 'cropper' to 
your INSTALLED_APPS tuple.

::

    INSTALLED_APPS += (
        'cropper',
    )

Next step add django-image-cropper URL config to your url module:

::

    urlpatterns = patterns('',
        ....
        url('^cropper/', include('cropper.urls')),
        ...
    )

And last call syncdb management command in your project:

::

    ./manage.py syncdb 

if you're use django v1.3 or later, you also collect static files:

::
    
    ./manage.py collecstatic
    

Otherwise you need copy django-image-cropper/cropper/media files into your
MEDIA_ROOT directory manually or create a symlink.


Usage
=====

Open /cropper/ URL in your browser. You can choose image and upload it. In
next page. If javascript is enabled and static serve works correct, you'll
jquery's jcrop plugin workspace. Select a picture region my means of mouse
and push 'Crop' button.

Image will be cropped and saved on server.


Customize crop logics
=====================

Of course, default logic is poor and unusable. But you can easy change
application behavior. 

You can write own success handlers for image upload and image crop and tell
django to use it.

To use own hanlders insead of defaults, just use own URLConfs. You must use
own 'success' key in keyword args. This value must be python callable type

::

    from cropper.forms import CroppedForm, UploadForm
    from my_project.utils import my_upload_handler, my_crop_handler

    urlpatterns = patterns('cropper.views',
        url('^$', view='upload', name='cropper_upload', kwargs={'form_class': UploadForm, 'success':  my_upload_handler}),
        url('^(?P<original_id>\d+)/$', view='crop', name='cropper_crop', kwargs={'form_class': CropForm, 'success':  my_crop_handler}),
    )


As you see, you can also use another form class instead of standart if you'll
specify 'form_class' key, but probably don't need this. 

What handler is it?

Each handler is python function which has some input arguments and returns
HttpResponse object like every view function.

Let's see to upload handler prototype:

::

    def my_upload_success_handler(request, form, original):
        """
        Success upload handler        
        """
        print "Uploda form data", form.cleaned_data
        print "File uploaded to " % original.image.path
        
        # This handler do nothing, but print parameters
        
        from django.shortcuts import redirect        
        return redirect(original)

* **request** is WSGIRequest object (same as view)
* **form** is upload form instance. This form instance is valid anyway.
* **original** is Original model instance. Image field calls ``image``

Crop handler prototype:

::

    def my_crop_success_handler(request, form, original, cropped):
        """
        Custom crop handler
        """
        print "Crop form data", form.cleaned_data
        print "Original object: %s" % original
        print "Original in cropped model (the same in previous line): %s" % cropped.original
        print "Cropped image: %s" % cropped.image

        # For example, we can use cropped image as user profile avatar
        # Perhaps user is authenticated and skip checks ;)

        from django.core.files.base import ContentFile
        from django.contrib import messages
        from django.shortcuts import redirect
        import os

        profile = request.user.get_profile()
        profile.avatar.save(
            os.path.basename(cropped.image.path),
            ContentFile(cropped.image.path)
        )
        
        messages.success(request, 'Avatar uploaded and cropped')
        return redirect(request.user)

First three arguments the same as upload handler input arguments. Fouth - is
**Cropped** model instance. It has ``image`` field containts cropped image and
foreign key to related Original photo.


Contributing
============

If you've found a bug, implemented a feature and think it is useful, then please
consider contributing. Patches, pull requests or just suggestions are welcome!
