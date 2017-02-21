from django.conf.urls import url
from .views import UserViewSet, ProfileViewSet

urlpatterns = [
    url(r'^user/$', UserViewSet.as_view({
        "post": "create",
        "get": "list"})),
    url(r'^user/(?P<pk>([0-9]+)|(current))/$', UserViewSet.as_view({
        "patch": "update",
        "get": "retrieve",
        "delete": "destroy"})),
    url(r'^user/(?P<user_id>[0-9]+)/profile/$', ProfileViewSet.as_view({
        "post": "create",
        "get": "list"})),
    url(r'^user/(?P<user_id>[0-9]+)/profile/(?P<pk>[0-9]+)/$', ProfileViewSet.as_view({
        "get": "retrieve",
        "delete": "destroy"})),
]
