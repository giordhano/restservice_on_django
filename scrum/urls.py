from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import include
from board.urls import router


urlpatterns = [
    # Examples:
    # url(r'^$', 'scrum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api/token/',obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
]
