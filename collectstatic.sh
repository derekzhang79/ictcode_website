#!/bin/sh

python manage.py collectstatic --noinput

yui-compressor --type=css static/django_utils/css/reset.css css/base.css > css/style.css

python manage.py collectstatic --noinput
