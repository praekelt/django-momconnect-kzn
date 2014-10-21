#!/bin/sh
export DATABASE_URL="sqlite://:memory:"
export DJANGO_SETTINGS_MODULE="momconnectkzn.testsettings"
./manage.py test "$@"
