# Generated by Django 3.0.5 on 2020-09-14 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professionalskills',
            old_name='skillDetail',
            new_name='skill_detail',
        ),
    ]
