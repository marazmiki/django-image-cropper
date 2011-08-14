#!/usr/bin/env python
from distutils.core import setup
import os

version='0.1'
package = 'cropper'

setup(
    name = 'django-image-cropper',
    version = version,
    author  = 'marazmiki',
    author_email = 'marazmiki@gmail.com',
    url = 'http://bitbucket.org/marazmiki/django-image-cropper/',
    download_url = 'http://bitbucket.org/marazmiki/django-image-cropper/get/tip.zip',

    description = 'This app allows upload and crop images',
    long_description = open('README.rst').read(),
    license = 'MIT license',
    requires = ['django (>=1.2)'],

    packages=['cropper'],
    package_data={
        'cropper': [
            'locale/ru/LC_MESSAGES/*',
            'media/cropper/*',
            'templates/cropper/*.html',
        ]
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
