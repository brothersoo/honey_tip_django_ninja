from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel
from honey_tip.settings import AUTH_USER_MODEL


class Category(TimeStampedModel):
    name = models.CharField(_('name'), max_length=30, null=False)

    class Meta:
        verbose_name = _('ht_category')
        verbose_name_plural = _('categories')
        db_table = 'category'


class Tip(TimeStampedModel):
    title = models.CharField(_('title'), max_length=50, null=False)
    content = models.CharField(_('content'), max_length=800, null=False)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class TipStatus(models.TextChoices):
        POSTED: tuple = 'PST', _('Posted')
        REMOVED: tuple = 'RMV', _('Removed')
        HIDDEN: tuple = 'HID', _('Hidden')
        REPORTED: tuple = 'RPT', _('Reported')

    status = models.CharField(_('status'), choices=TipStatus.choices, max_length=3, default=TipStatus.POSTED)

    class Meta:
        verbose_name = _('ht_tip')
        verbose_name_plural = _('tips')
        db_table = _('tip')


class Report(TimeStampedModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE)

    class ReportStatus(models.TextChoices):
        PENDING: tuple = 'PND', _('Pending')
        REJECTED: tuple = 'RJT', _('Rejected')
        APPROVED: tuple = 'APV', _('Approved')

    status = models.CharField(_('status'), choices=ReportStatus.choices, max_length=3, default=ReportStatus.PENDING)

    class Meta:
        verbose_name = _('ht_report')
        verbose_name_plural = _('reports')
        db_table = _('report')

