# Generated by Django 2.2.5 on 2019-09-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
