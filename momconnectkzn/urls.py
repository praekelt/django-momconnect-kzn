from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    # TastyPie breaks if a namespace is set. See
    # https://github.com/toastdriven/django-tastypie/issues/24
    url(r'^servicerating/', include('servicerating.urls')),
)
