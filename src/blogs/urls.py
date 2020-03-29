from django.conf.urls import url

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blogs'

urlpatterns = [
    url(r'^$',BlogListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$',BlogDetailView.as_view(), name='detail'),
    url(r'^create/$',BlogCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update/$',BlogUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',BlogDeleteView.as_view(), name='delete'),
]
