from django.db import models

from main.models import Poll


class Question(models.Model):
    # should it be allowed to create a question without any text?

    CHOICE_TYPES = (
        ('open', 'Ответ текстом'),
        ('single', 'Один вариант ответа'),
        ('multiple', 'Несколько вариантов ответа'),
    )

    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=255, blank=True)
    choice_type = models.CharField(max_length=10, choices=CHOICE_TYPES)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.choice_type}'


