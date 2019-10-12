"""blogproject_files URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include

import blog.views as ve

#正则表达式匹配传入的请求路径，匹配成功则进入对应的view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog', ve.myPage),  #由于目前只有一个app, 方便起见, 就不设置include了
    # url(r'^(?P<my_args>\d+)/$', ve.detail), #匹配路径前面的数字，如果匹配成功进入试图
    url(r'^dev1',ve.sqlQuery),
    url(r'^test',ve.myTemplate),
    url(r'^home$',ve.home),
    url(r'^(?P<id>\d+)/$', ve.demo) #P<id>即使一个参数
]
