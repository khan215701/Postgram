# Generated by Django 4.2.5 on 2023-10-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0002_user_avatar_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]