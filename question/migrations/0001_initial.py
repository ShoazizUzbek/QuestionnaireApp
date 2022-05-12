# Generated by Django 4.0.2 on 2022-05-11 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Questionier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.guest')),
                ('questioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.questionier')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.CharField(max_length=255)),
                ('questionier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='question.questionier')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.CharField(max_length=255)),
                ('submitted_time', models.DateTimeField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.questionsession')),
            ],
        ),
    ]