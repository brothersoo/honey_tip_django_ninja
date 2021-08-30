from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .settings import AUTH_USER_MODEL


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)
    nickname = models.CharField(_('nickname'), max_length=50, unique=True, null=False)

    class UserStatus(models.TextChoices):
        ACTIVE: tuple = 'ACT', _('Active')
        BANNED: tuple = 'BAN', _('Banned')
        QUIT: tuple = 'QIT', _('Quit')

    status = models.CharField(_('status'), choices=UserStatus.choices, max_length=3, default=UserStatus.ACTIVE)

    class Meta(AbstractUser.Meta):
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'user'


class Category(TimeStampedModel):
    name = models.CharField(_('name'), max_length=30, null=False)

    class Meta:
        verbose_name = _('category')
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
        verbose_name = _('tip')
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
        verbose_name = _('report')
        verbose_name_plural = _('reports')
        db_table = _('report')

