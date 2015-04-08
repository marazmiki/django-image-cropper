#!/usr/bin/env python
# coding: utf-8

from django.conf import settings
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


settings.configure(
    DEBUG=False,
    ROOT_URLCONF='cropper.urls',
    MIDDLEWARE_CLASSES=(),
    STATIC_URL='/static/',
    CROPPER_ROOT='.',
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'cropper',
    ),
    DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':MEMORY:'
        }
    })


def main():
    from django.test.utils import get_runner
    import django

    if hasattr(django, 'setup'):
        django.setup()

    find_pattern = 'cropper'

    test_runner = get_runner(settings)(verbosity=2, interactive=True)
    failed = test_runner.run_tests([find_pattern])
    sys.exit(failed)


if __name__ == '__main__':
    main()
