# Generated by Django 3.2.4 on 2022-06-29 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newProduct', '0019_color_adjacent_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='adjacent_color',
        ),
        migrations.AddField(
            model_name='adjacentcolor',
            name='parent_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='adjacent_color', to='newProduct.color'),
        ),
    ]