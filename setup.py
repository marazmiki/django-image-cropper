#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import os


version = '0.4.0'
package = 'cropper'

path = os.path.join(os.path.dirname(__file__), 'cropper')
setuptools.setup(
    name='django-image-cropper',
    version=version,
    author='marazmiki',
    author_email='marazmiki@gmail.com',
    url='http://pypi.python.org/pypi/django-image-cropper/',
    download_url=('http://bitbucket.org/marazmiki/django-'
                  'image-cropper/get/tip.zip'),
    description='This app allows upload and crop images',
    long_description=open('README.rst').read(),
    license='MIT license',
    install_requires=['django>=1.5', 'Pillow', 'dj-upload-to'],
    tests_require=['dj-inmemorystorage'],
    packages=setuptools.find_packages(),
    test_suite='tests.main',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
