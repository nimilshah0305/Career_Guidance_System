# Generated by Django 3.0.5 on 2020-05-14 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forward', '0010_remove_profileresult_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileevaluation',
            name='email',
        ),
    ]
