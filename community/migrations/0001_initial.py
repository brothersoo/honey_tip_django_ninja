# Generated by Django 3.2.6 on 2021-08-30 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
            options={
                'verbose_name': 'ht_category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('content', models.CharField(max_length=800, verbose_name='content')),
                ('status', models.CharField(choices=[('PST', 'Posted'), ('RMV', 'Removed'), ('HID', 'Hidden'), ('RPT', 'Reported')], default='PST', max_length=3, verbose_name='status')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='community.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ht_tip',
                'verbose_name_plural': 'tips',
                'db_table': 'tip',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('status', models.CharField(choices=[('PND', 'Pending'), ('RJT', 'Rejected'), ('APV', 'Approved')], default='PND', max_length=3, verbose_name='status')),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.tip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ht_report',
                'verbose_name_plural': 'reports',
                'db_table': 'report',
            },
        ),
    ]