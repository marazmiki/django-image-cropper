from django.conf import settings

ROOT = getattr(settings, 'CROPPER_ROOT', 'cropped/').rstrip('/')
MAX_WIDTH  = getattr(settings, 'CROPPER_MAX_WIDTH',  1680)
MAX_HEIGHT = getattr(settings, 'CROPPER_MAX_HEIGHT', 1024)
ALLOWED_DIMENSIONS = getattr(settings, 'CROPPER_ALLOWED_DIMENSIONS', ())

SHOW_ADMIN = getattr(settings, 'CROPPER_SHOW_ADMIN', True)
