# Generated by Django 3.2.9 on 2022-05-12 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_rename_questionier_question_questionnaire'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answerrecord',
            unique_together={('session', 'question')},
        ),
    ]
