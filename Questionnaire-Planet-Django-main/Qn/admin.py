from django.contrib import admin

from .models import *

admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(Option)
admin.site.register(Answer)
admin.site.register(Submit)
# 在此处注册您的模型。
