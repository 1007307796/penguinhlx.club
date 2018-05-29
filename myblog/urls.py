"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from blog.feeds import AllPostsRssFeed

# 当新建一个应用的时候必须包含在总urls.py文件里面
urlpatterns = [
    path('', include('comments.urls')),
    path('search/', include('haystack.urls')),
    path('all/rss/', AllPostsRssFeed(), name='rss'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

]
