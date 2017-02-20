from django.conf.urls import url
from .views import UserViewSet

urlpatterns = [
    url(r'^$', UserViewSet.as_view({
        "post": "create",
        "get": "list"})),
    url(r'^(?P<pk>([0-9]+)|(current))/$', UserViewSet.as_view({
        "patch": "update",
        "get": "retrieve",
        "delete": "destroy"})),
]
