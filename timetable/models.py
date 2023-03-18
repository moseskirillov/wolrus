from django.db import models
from wagtail.models import Page


class Calendar(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']

    class Meta:
        verbose_name = 'Календарь'


class Event(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Название')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания')
    active = models.BooleanField(default=False, verbose_name='Активно')

    def __str__(self):
        return 'Событие'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
