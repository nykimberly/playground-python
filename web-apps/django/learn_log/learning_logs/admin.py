from django.contrib import admin

from learning_logs.models import Topic, Entry

# Tell django to manage our Topic and Entry models through admin site
admin.site.register(Topic)
admin.site.register(Entry)
