# Generated by Django 4.2.11 on 2024-05-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.BigIntegerField(default='0'),
        ),
    ]