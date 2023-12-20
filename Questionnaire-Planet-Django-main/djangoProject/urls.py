"""djangoProject URL 配置

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
例子：
函数视图
    1. 添加导入：从my_app导入视图
    2. 向 urlpatterns 添加 URL：path（''， views.home， name='home'）
基于类的视图
    1. 添加导入：from other_app.views import Home
    2. 向 urlpatterns 添加 URL：path（''， Home.as_view（）， name='home'）
包括另一个 URLconf
    1. 导入 include（） 函数：from django.urls import include， path
    2. 向 urlpatterns 添加 URL：path（'blog/'， include（'blog.urls'））
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

#from django.conf.urls import url
from django.urls import re_path as url

from django.views.static import serve

import Qn.views
import resources.views

urlpatterns = [
    path('api/qs/admin/', admin.site.urls),
    path('api/qs/user/', include(('userinfo.urls', 'userinfo'))),
    path('api/qs/qn/', include(('Qn.urls', 'Qn'))),
    path('api/qs/sm/', include(('Submit.urls', 'Submit'))),
    path('api/qs/all_count/submit', Qn.views.all_submittion_count),
    path('api/qs/sp/', include(('signup.urls', 'signup'))),
    path('api/qs/ep/', include(('epidemic.urls', 'epidemic'))),

    path('api/qs/upload/image', resources.views.upload_image),
    path('api/qs/upload/video', resources.views.upload_video),

    url(r'media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


