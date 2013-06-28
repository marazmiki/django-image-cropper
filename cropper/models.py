from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.conf import settings as django_settings
from cropper import settings
import Image
import os
import uuid

def dimension_validator(image):
    """
    """
    if settings.MAX_WIDTH != 0 and image.width > settings.MAX_WIDTH:
        raise ValidationError(_('Image width greater then allowed'))

    if settings.MAX_HEIGHT != 0 and image.height > settings.MAX_HEIGHT:
        raise ValidationError(_('Image height greater then allowed'))


class Original(models.Model):
    def upload_image(self, filename):
        return u'{path}/{name}.{ext}'.format(path=settings.ROOT,
                                             name=uuid.uuid4().hex,
                                             ext=os.path.splitext(filename)[1].strip('.'))

    def __unicode__(self):
        return unicode(self.image)

    @models.permalink
    def get_absolute_url(self):
        return 'cropper_crop', [self.pk]    

    image = models.ImageField(_('Original image'),
                            upload_to=upload_image,
                            width_field='image_width',
                            height_field='image_height',
                            validators=[dimension_validator])
    image_width = models.PositiveIntegerField(_('Image width'),
                                                editable=False,
                                                default=0)
    image_height = models.PositiveIntegerField(_('Image height'),
                                               editable=False,
                                               default=0)


class Cropped(models.Model):
    def __unicode__(self):
        return u'%s-%sx%s' % (self.original, self.w, self.h)

    def upload_image(self, filename):
        return '%s/crop-%s' % (settings.ROOT, filename)

    def save(self, *args, **kwargs):
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
                                 related_name='cropped',
                                 verbose_name=_('Original image'))
    image = models.ImageField(_('Image'),
                              upload_to=upload_image,
                              editable=False)
    x = models.PositiveIntegerField(_('offset X'),
                                   default=0)
    y = models.PositiveIntegerField(_('offset Y'),
                                   default=0)
    w = models.PositiveIntegerField(_('cropped area width'),
                                    blank=True,
                                    null=True)
    h = models.PositiveIntegerField(_('cropped area height'),
                                    blank=True,
                                    null=True)

    class Meta(object):
        verbose_name = _('cropped image')
        verbose_name_plural = _('cropped images')

