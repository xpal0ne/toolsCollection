from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'JenkinsDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^node/', 'jenkinsHandle.views.node_list'),
    url(r'^index/', 'jenkinsHandle.views.job_list'),
    url(r'^log_check', 'logworker.views.log_check'),
    url(r'^log/', 'logworker.views.show_index'),
    url(r'^interface/', 'interfaceChecker.views.show_index')
]
