#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import os

version='0.1.2'
package = 'cropper'

path = os.path.join(os.path.dirname(__file__), 'cropper')
print path
print setuptools.find_packages()
setuptools.setup(
    name = 'django-image-cropper',
    version = version,
    author  = 'marazmiki',
    author_email = 'marazmiki@gmail.com',
    url = 'http://bitbucket.org/marazmiki/django-image-cropper/',
    download_url = 'http://bitbucket.org/marazmiki/django-image-cropper/get/tip.zip',

    description = 'This app allows upload and crop images',
    long_description = open('README.rst').read(),
    license = 'MIT license',
    install_requires = ['django>=1.2.5', 'PIL'],

    packages = setuptools.find_packages(),
        include_package_data=True,
#    package_dir={'cropper':  path},
#    package_data = { 'cropper': [
#        'locale/ru/LC_MESSAGES/*',
#        'static/cropper/js/*',
#        'static/cropper/css/*',
#        'static/cropper/img/*',
#        'templates/cropper/*',
#        'templates/admin/cropper/cropped/*',
#    ]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
