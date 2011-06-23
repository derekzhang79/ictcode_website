#!/bin/sh

python manage.py collectstatic --noinput

yui-compressor --type=css static/django_utils/css/reset.css > css/style.css
yui-compressor --type=css css/base.css >> css/style.css
