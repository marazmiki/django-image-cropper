from django.db import settings
from cropper.defaults import upload_success, crop_success

ROOT = getattr(settings, 'CROPPER_ROOT', 'cropped/').rstrip('/')
MAX_WIDTH  = getattr(settings, 'CROPPER_MAX_WIDTH',  1680)
MAX_HEIGHT = getattr(settings, 'CROPPER_MAX_HEIGHT', 1024)
ALLOWED_DIMENSIONS = getattr(settings, 'CROPPER_ALLOWED_DIMENSIONS', ())

UPLOAD_SUCCESS = upload_success
CROP_SUCCESS   = crop_success
SHOW_ADMIN = getattr(settings, 'CROPPER_SHOW_ADMIN', True)
