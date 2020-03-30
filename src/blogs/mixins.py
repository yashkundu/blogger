from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .models import Blog

class UpdatePermissionMixin(object):

    def dispatch(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=self.kwargs.get('pk'))
        if request.user != blog.user:
            raise PermissionDenied('You are not allowed to access this.')
        return super(UpdatePermissionMixin, self).dispatch(request, *args, **kwargs)
