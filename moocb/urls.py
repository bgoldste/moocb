from django.conf.urls import patterns, include, url
from django.contrib import admin
from moocb.views import home, login_user, me, logout_user, add_time
from django.conf import settings

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
    url(r'^add/$', add_time),

)


urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
