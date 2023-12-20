from django.contrib import admin

from .models import *
# 在此处注册您的模型。

admin.site.register(User)
admin.site.register(ConfirmString)
