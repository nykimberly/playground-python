from django.contrib import admin

from learning_logs.models import Topic

# Tell django to manage our Topic model through admin site
admin.site.register(Topic)
