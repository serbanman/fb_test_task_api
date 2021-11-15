from django.contrib import admin
from main.models import Poll, Question


class PollAdmin(admin.ModelAdmin):
    readonly_fields = ('start_date',)


admin.site.register(Poll, PollAdmin)
admin.site.register(Question)
