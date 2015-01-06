from django.conf.urls import patterns, include, url
from django.contrib import admin
from moocb.views import home, login_user, me, logout_user, add_time, add_user, add_goal, login_user_json, select_goal, add_incentive, pay
from django.conf import settings
from django.views.generic import TemplateView


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
    url(r'^adduser/$', add_user),
    url(r'^addgoal/$', add_goal),
    url(r'^addincentive/$', add_incentive),
    url(r'^login_json/$', login_user_json),
    url(r'^select_goal/$', select_goal),
    url(r'^pay/$', pay),
  

     url(r'^google6f82ca7c7de8dd2c.html/$', TemplateView.as_view(template_name='moocb/google6f82ca7c7de8dd2c.html'), name="home"),
      url(r'^google7c1c3385afed65d5.html/$', TemplateView.as_view(template_name='moocb/google7c1c3385afed65d5.html'), name="home"),

)


urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
