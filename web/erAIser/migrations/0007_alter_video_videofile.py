# Generated by Django 3.2.5 on 2021-07-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erAIser', '0006_rename_content_video_videofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(null=True, upload_to='video/'),
        ),
    ]
