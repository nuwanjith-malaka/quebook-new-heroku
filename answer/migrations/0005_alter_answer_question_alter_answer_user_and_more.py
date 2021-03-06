# Generated by Django 4.0 on 2022-03-02 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_alter_questioncomment_question'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('answer', '0004_alter_answercomment_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='question.question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_comments', to='auth.user'),
        ),
    ]
