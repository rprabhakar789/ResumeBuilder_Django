# Generated by Django 3.0.5 on 2020-09-17 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_person_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='person',
            name='github',
        ),
        migrations.RemoveField(
            model_name='person',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='person',
            name='mobile',
        ),
        migrations.CreateModel(
            name='ProfileInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=20)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Person')),
            ],
        ),
    ]
