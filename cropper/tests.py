# coding: utf-8

from django import test
from django.conf import settings
from django.core.urlresolvers import reverse
from cropper.models import Original, Cropped
from django.core.files.base import ContentFile
from PIL import Image
import os
import json


CROP_X = 304
CROP_Y = 151
CROP_W = 175
CROP_H = 193

MAX_WIDTH = 1680
MAX_HEIGHT = 1024


def get_filename(name='original.jpg'):
    """
    Returns the full path to test images
    """
    return os.path.join(os.path.dirname(__file__), 'tests', name)


class BaseTestCase(test.TestCase):
    urls = 'cropper.urls'

    def setUp(self):
        self.client = test.Client()
        self.url = reverse('cropper_upload')


class ModelTest(test.TestCase):
    def create_original(self):
        with open(self.filename, 'rb') as fp:
            original = Original()
            original.image.save(
                os.path.basename(self.filename),
                ContentFile(fp.read())
            )
        return original

    def setUp(self):
        self.filename = get_filename()
        self.original = self.create_original()

    def tearDown(self):
        settings.CROPPER_MAX_WIDTH = MAX_WIDTH
        settings.CROPPER_MAX_HEIGHT = MAX_HEIGHT

    def test_original_max_width_exceed(self):
        settings.CROPPER_MAX_WIDTH = 30
        self.original = self.create_original()

    def test_original(self):
        source = Image.open(self.filename)
        original = Image.open(self.original.image)
        self.assertEqual(source.size, original.size)
        self.assertEqual(source.format, original.format)

#        self.assertTrue(filecmp.cmp(self.filename, self.original.image.path))

    def test_cropped(self):
        cropped = Cropped.objects.create(
            original=self.original,
            w=CROP_W,
            h=CROP_H,
            x=CROP_X,
            y=CROP_Y)

        orig = Image.open(get_filename('cropped_304-151-175-193.jpg'))
        crop = Image.open(cropped.image)

        self.assertEqual(orig.size, crop.size)


class UploadTestCase(BaseTestCase):
    def upload_scenario(self):
        page = self.client.get(self.url)

        self.assertEquals(200, page.status_code)
        self.assertIn('form', page.context)
        self.assertIn('multipart/form-data', page.content)
        self.assertIn('submit', page.content)

        page = self.client.post(self.url, data={
            'image': open(get_filename())
        }, follow=True)

        self.assertEquals(200, page.status_code)
        self.assertIn('form', page.context)
        self.assertIn('original', page.context)
        return page.context['original']

    def test_crop_without_ahax(self):
        original = self.upload_scenario()
        page = self.client.post(original.get_absolute_url(), data={
            'original': original.pk,
            'x': CROP_X,
            'y': CROP_Y,
            'w': CROP_W,
            'h': CROP_H
        })

        self.assertIn('original', page.context)
        self.assertIn('cropped', page.context)

        with open(get_filename('cropped_304-151-175-193.jpg'), 'rb') as fp:
            self.assertEqual(
                Image.open(fp).size,
                Image.open(page.context['cropped'].image).size
            )

    def test_ajax_crop(self):
        original = self.upload_scenario()
        page = self.client.post(original.get_absolute_url(),
                                data={'original': original.pk,
                                      'x': CROP_X,
                                      'y': CROP_Y,
                                      'w': CROP_W,
                                      'h': CROP_H},
                                HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        data = json.loads(page.content)

        self.assertIn('image', data)
        self.assertIn('url', data['image'])
        self.assertIn('width', data['image'])
        self.assertIn('height', data['image'])
        self.assertEquals(CROP_W, data['image']['width'])
        self.assertEquals(CROP_H, data['image']['height'])
