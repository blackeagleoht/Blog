from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from .views import IndexView,ArichiveView,TagView,TagDetailView,CategoryView
from .views import BlogDetailView,AddCommentView,CategoryDetaiView,MySearchView 
from .feeds import BlogRssFeed

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),  #首页的url
    url(r'^archive/$', ArichiveView.as_view(), name='archive'),
    url(r'^tags/$', TagView.as_view(), name='tags'),
    url(r'^tags/(?P<tag_name>\w+)$', TagDetailView.as_view(), name='tag_name'),
    url(r'^blog/(?P<blog_id>\d+)$', BlogDetailView.as_view(), name='blog_id'),
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    url(r'^rss/$', BlogRssFeed(), name='rss'),
    url(r'^category/(?P<category_name>\w+)$', CategoryDetaiView.as_view(), name='category_name'),
    url(r'^search/', MySearchView(),  name='haystack_search'),
    url(r'^categorys/$', CategoryView.as_view(), name='categorys'),
]


# 配置全局404页面
hander404 = 'myblog.views.page_not_found'

# 配置全局505页面
hander505 = 'myblog.views.page_errors'
