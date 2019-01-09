from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import SimpleRouter
from todo import views


# Remove final trailing slash
class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()

router = OptionalSlashRouter()
schema_view = get_swagger_view(title='TODO')

router.register(r'^task', views.TaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$', views.status),
    url(r'^ping', views.ping),
    url(r'^docs', schema_view),
    url(r'^admin', admin.site.urls),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework'))
]

# Serve static
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, }),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT }),
]
