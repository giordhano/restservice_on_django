from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Examples:
    # url(r'^$', 'scrum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^api/token/',obtain_auth_token, name='api-token')
]
