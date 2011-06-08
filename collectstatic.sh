#!/bin/sh

python manage.py collectstatic --noinput

mkdir -p static/min/

yui-compressor --type=css static/django_utils/css/reset.css > static/min/reset-min.css
yui-compressor --type=css static/style.css > static/min/style-min.css

cat static/min/reset-min.css > static/style.css
cat static/min/style-min.css >> css/style.css

rm -r static/min/
