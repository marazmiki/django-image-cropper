# -*- coding: utf-8 -*

from django import template

import re

register = template.Library()

DIM_RE = re.compile('\[(?P<x>\d+)?,(?P<y>\d+)?\]')
AR_RE = re.compile('^(?P<x>\f)/(?P<y>\f)$')
ARP_RE = re.compile('^(?P<a>\f)$')

@register.simple_tag
def allowed_dimension_data(dimstr):
    """
    return html5 data attributes data-minSize='[x,y]'
    and/or data-aspectRatio='x/y' based on input string of
    [x,y] - absolute width/height
    [x,0] - set width only
    [0,y] - set height only
    x/y - aspect ration as eq.
    a - aspect ration as float
    """
    dims = ''
    ar = ''
    returnstr = ''
    dim_match = DIM_RE.match(dimstr)
    ar_match = AR_RE.match(dimstr)
    arp_match = ARP_RE.match(dimstr)
    if dim_match:
        dims = dimstr
        if dim_match.group('x') is not None and dim_match.group('y'):
            ar = float(dim_match.group('x'))/float(dim_match.group('y'))
    elif ar_match:
        ar = int(ar_match.group('x'))/int(ar_match.group('y'))
    elif arp_match:
        ar = float(arp_match.group('a'))
    else:
        return ''
    
    if dims:
        returnstr = 'data-minSize="%s" ' % dims
    if ar:
        returnstr += 'data-aspectRatio="%f"' % ar
    
    return returnstr
