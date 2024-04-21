# Generated by Django 5.0.1 on 2024-04-18 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0010_coursepayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepayment',
            name='name',
            field=models.ForeignKey(blank=True, default=4, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='название курса'),
        ),
    ]