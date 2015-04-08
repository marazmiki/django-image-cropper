# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

try:
    from django.http import JsonResponse
except ImportError:
    from django.http import HttpResponse
    import json

    class JsonResponse(HttpResponse):
        def __init__(self, data, **kwargs):
            kwargs.setdefault('content_type', 'application/json')
            super(JsonResponse, self).__init__(json.dumps(data), **kwargs)
