# Generated by Django 3.2.4 on 2022-07-21 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]