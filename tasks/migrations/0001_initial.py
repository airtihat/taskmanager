# Generated by Django 5.2.3 on 2025-06-26 20:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان المهمة')),
                ('description', models.TextField(blank=True, null=True, verbose_name='تفاصيل المهمة')),
                ('due_date', models.DateField(verbose_name='تاريخ التنفيذ')),
                ('completed', models.BooleanField(default=False, verbose_name='تمت؟')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
