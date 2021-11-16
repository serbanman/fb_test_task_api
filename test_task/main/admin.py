from django.contrib import admin
from main.models import Poll, Question, Answer, RespondentUser


class PollAdmin(admin.ModelAdmin):
    # model manager created to made start_date read only after the entry creation
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['start_date']
        else:
            return []


admin.site.register(Poll, PollAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(RespondentUser)
