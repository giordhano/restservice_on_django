
from django.contrib.auth import get_user_model

from rest_framework import authentication, permissions,viewsets

from .models import Sprint,Task
from .serializers import sprintSerializer, taskSerializer, UserSerializer 

User = get_user_model()

class DefaultsMixin(object):
    
    authentication_clases = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )

    paginate_by = 25



class SprintViewSet( DefaultsMixin, viewsets.ModelViewSet):

    queryset = Sprint.objects.order_by('end')
    serializer_class= sprintSerializer



class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = taskSerializer


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer