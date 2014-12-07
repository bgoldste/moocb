from django.conf.urls import patterns, include, url
from django.contrib import admin
from moocb.views import home, login_user, me, logout_user


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moocb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^login/$', login_user),
    url(r'^logout/$', logout_user),
    url(r'^me/$', me),
)
