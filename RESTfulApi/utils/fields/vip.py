#!/usr/bin/env python
# encoding: utf-8

"""
    File name: vip.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask.ext.restful import fields


vip_fields = {
    'id': fields.String,
    'username': fields.String,
    'nickname': fields.String,
    'phone': fields.String,
}

# for get /vips
vips_fields = {
    'vips': fields.List(fields.Nested(vip_fields))
}
