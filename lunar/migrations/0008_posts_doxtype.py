# Generated by Django 3.2.5 on 2022-07-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunar', '0007_alter_teacher_officenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='doxtype',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]