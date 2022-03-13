# Generated by Django 4.0 on 2022-01-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_alter_question_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.CharField(choices=[('Buddhism', 'Buddhism'), ('Sinhala', 'Sinhala'), ('English', 'English'), ('Mathematics', 'Mathematics'), ('Geography', 'Geography'), ('Science', 'Science'), ('Commerce', 'Commerce'), ('Agriculture', 'Agriculture'), ('ICT', 'ICT'), ('Drama', 'Drama'), ('Art', 'Art'), ('Dance', 'Dance'), ('History', 'History'), ('Music', 'Music'), ('Health', 'Health'), ('Tamil', 'Tamil')], default='Buddhism', max_length=15),
        ),
    ]
