from django.contrib import admin
from learning_logs.models import Topic, Entry
# 在这里注册你的模型
admin.site.register(Topic)
admin.site.register(Entry)

