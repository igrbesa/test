from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'map.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^poc', 'article.views.poc', name = 'poc'),
    url(r'^extemplate', 'article.views.extemplate', name = 'extemplate'),
    url(r'^listdb', 'article.views.listdb', name = 'listdb'),
    url(r'^adduser', 'article.views.adduser', name = 'adduser'),
    url(r'^admin/', include(admin.site.urls)),
)
