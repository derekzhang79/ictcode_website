#!/bin/sh

optipng -o3 img/*.png
advpng -z -4 img/*.png
advdef -z -4 img/*.png
