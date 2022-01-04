# Generated by Django 4.0.1 on 2022-01-04 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='homeworkresult',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='polls.student'),
        ),
        migrations.AlterField(
            model_name='homeworkresult',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='homeworkresult',
            name='homework',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='polls.homework'),
        ),
    ]
