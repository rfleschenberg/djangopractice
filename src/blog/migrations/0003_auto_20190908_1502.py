# Generated by Django 2.2.5 on 2019-09-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.IntegerField(default=2),
        ),
    ]