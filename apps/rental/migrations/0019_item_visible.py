# Generated by Django 3.2.4 on 2022-03-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0018_alter_item_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]