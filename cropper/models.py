from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.conf import settings as django_settings
from cropper import settings
import Image
import os

def dimension_validator(image):
    """
    """
    if settings.MAX_WIDTH != 0 and image.width > settings.MAX_WIDTH:
        raise ValidationError, _('Image width greater then allowed')

    if settings.MAX_HEIGHT != 0 and image.height > settings.MAX_HEIGHT:
        raise ValidationError, _('Image height greater then allowed')

class Original(models.Model):
    def upload_image(self, filename):
        return '%s/%s' % (settings.ROOT, filename)

    def __unicode__(self):
        return unicode(self.image)

    def get_absolute_url(self):
        return 'cropper_crop', [self.pk]    
    get_absolute_url = models.permalink(get_absolute_url)

    image = models.ImageField(_('Original image'),
        upload_to    = upload_image,
        width_field  = 'image_width',
        height_field = 'image_height',
        validators   = [dimension_validator])
    image_width = models.PositiveIntegerField(_('Image width'),
        editable = False,
        default = 0)
    image_height = models.PositiveIntegerField(_('Image height'),
        editable = False,
        default = 0)

class Cropped(models.Model):
    def __unicode__(self):
        return u'%s-%sx%s' % (self.original, self.w, self.h)

    def upload_image(self, filename):
        return '%s/crop-%s' % (settings.ROOT, filename)

    def save(self, *args, **kwargs): #force_insert=False, force_update=False, using=None):
        source = self.original.image.path
        target = self.upload_image(os.path.basename(source))

        Image.open(source).crop([
            self.x,             # Left
            self.y,             # Top
            self.x + self.w,    # Right
            self.y + self.h     # Bottom
        ]).save(django_settings.MEDIA_ROOT + os.sep + target)

        self.image = target        
        super(Cropped, self).save(*args, **kwargs)

    original = models.ForeignKey(Original,
        related_name = 'cropped',
        verbose_name = _('Original image'))
    image = models.ImageField(_('Image'),
        upload_to = upload_image,
        editable  = False)
    x = models.PositiveIntegerField(_('Offset X'),
        default = 0)
    y = models.PositiveIntegerField(_('Offset Y'),
        default = 0)
    w = models.PositiveIntegerField(_('Cropped area width'),
        blank = True,
        null = True)
    h = models.PositiveIntegerField(_('Cropped area height'),
        blank = True,
        null = True)

    class Meta:
        verbose_name = _('cropped image')
        verbose_name_plural = _('cropped images')
