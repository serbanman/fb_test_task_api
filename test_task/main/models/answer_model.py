from django.db import models

from main.models import Question, RespondentUser


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(
        Question,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    respondent_user = models.ForeignKey(
        RespondentUser,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    answer_text = models.CharField(max_length=255, blank=False, null=True)