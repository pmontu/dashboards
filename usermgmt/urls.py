from django.conf.urls import url

from .views import UserViewSet

urlpatterns = [
    url(r'^$', UserViewSet.as_view({
    		"get": "list",
    		"post": "create"
    	})),
    url(r'^(?P<pk>[0-9]+)/$', UserViewSet.as_view({
    		"patch": "update",
    		"get": "retrieve",
    		"delete": "destroy"
    	})),
]
