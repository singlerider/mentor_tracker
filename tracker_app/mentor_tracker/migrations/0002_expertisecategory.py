# Generated by Django 2.1.7 on 2019-02-18 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertiseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Expertise categories',
            },
        ),
    ]
