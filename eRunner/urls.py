from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eRunner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/', 'django.contrib.auth.views.login', {'template_name':'login.html'}),

    url(r'^eRunner/', 'eHome.views.eRunner'),

)
