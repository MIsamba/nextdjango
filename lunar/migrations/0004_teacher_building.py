# Generated by Django 3.2.8 on 2022-06-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunar', '0003_auto_20220628_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='building',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
