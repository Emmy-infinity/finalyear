# Generated by Django 4.2.5 on 2023-09-27 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearningplatform', '0003_videotutorial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videotutorial',
            old_name='titele',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='videotutorial',
            old_name='video',
            new_name='videoclip',
        ),
    ]
