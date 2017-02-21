from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
from .views import home
from usermgmt import urls as usermgmt_urls

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    # url(r'^$', hello.views.index, name='index'),
    url(r'^$', home),
    url(r'^db/$', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(usermgmt_urls)),
]
