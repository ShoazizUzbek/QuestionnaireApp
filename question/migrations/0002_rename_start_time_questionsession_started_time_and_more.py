# Generated by Django 4.0.2 on 2022-05-11 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionsession',
            old_name='start_time',
            new_name='started_time',
        ),
        migrations.AddField(
            model_name='answerrecord',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='question.question'),
            preserve_default=False,
        ),
    ]
