# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.db import models
from django.utils import six
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from dj_upload_to import upload
from cropper import settings
from PIL import Image


def dimension_validator(image):
    """
    """
    if settings.MAX_WIDTH != 0 and image.width > settings.MAX_WIDTH:
        raise ValidationError(_('Image width greater then allowed'))

    if settings.MAX_HEIGHT != 0 and image.height > settings.MAX_HEIGHT:
        raise ValidationError(_('Image height greater then allowed'))


@python_2_unicode_compatible
class Original(models.Model):
    """
    The original image
    """
    image = models.ImageField(
        verbose_name=_('Original image'), upload_to=upload,
        width_field='image_width', height_field='image_height',
        validators=[dimension_validator])
    image_width = models.PositiveIntegerField(
        verbose_name=_('Image width'), editable=False, default=0)
    image_height = models.PositiveIntegerField(
        verbose_name=_('Image height'), editable=False, default=0)

    def __str__(self):
        return six.text_type(self.image)

    @models.permalink
    def get_absolute_url(self):
        return 'cropper_crop', [self.pk]

    class Meta(object):
        app_label = 'cropper'
        verbose_name = _('original')
        verbose_name_plural = _('originals')


@python_2_unicode_compatible
class Cropped(models.Model):
    """
    Cropped segment of original image
    """
    original = models.ForeignKey(Original, related_name='cropped',
                                 verbose_name=_('Original image'))
    image = models.ImageField(_('Image'), upload_to=upload,
                              editable=False)
    x = models.PositiveIntegerField(_('offset X'), default=0)
    y = models.PositiveIntegerField(_('offset Y'), default=0)
    w = models.PositiveIntegerField(_('cropped area width'),
                                    blank=True, null=True)
    h = models.PositiveIntegerField(_('cropped area height'),
                                    blank=True, null=True)

    def __str__(self):
        return u'%s-%sx%s' % (self.original, self.w, self.h)

    class Meta(object):
        app_label = 'cropper'
        verbose_name = _('cropped image')
        verbose_name_plural = _('cropped images')


def create_cropped_image(**kwargs):
    cropped = kwargs['instance']
    original = cropped.original
    cropped_stream = six.BytesIO()

    im = Image.open(original.image)
    crop_im = im.crop([
        cropped.x,                # Left
        cropped.y,                # Top
        cropped.x + cropped.w,    # Right
        cropped.y + cropped.h     # Bottom
    ])

    crop_im.save(cropped_stream, format=im.format)

    cropped_stream.seek(0)
    cropped.image.save(upload(cropped, original.image.url),
                       ContentFile(cropped_stream.read()), False)


def reload_model_data(**kwargs):
    kwargs['instance'] = Cropped.objects.get(pk=kwargs['instance'].pk)


models.signals.pre_save.connect(create_cropped_image, sender=Cropped,
                                dispatch_uid='cropper.models')
models.signals.post_save.connect(reload_model_data, sender=Cropped,
                                 dispatch_uid='cropper.models')
