from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # url(r'^$', 'sample.views.home', name='home'),
    # url(r'^sample/', include('sample.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
