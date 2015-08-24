from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'JenkinsDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^node/', 'jenkinsHandle.views.node_list'),
    url(r'^index/', 'jenkinsHandle.views.job_list'),
]
