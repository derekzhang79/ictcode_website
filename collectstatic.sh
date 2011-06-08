#!/bin/sh

yui-compressor --type=css css/style.css > css/style-min.css

cat css/style-min.css >> css/main-min.css

python manage.py collectstatic --noinput
