# Generated by Django 3.0.3 on 2020-04-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_post_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
