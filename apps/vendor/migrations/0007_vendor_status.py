# Generated by Django 3.2.4 on 2022-03-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_alter_userwishlist_is_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='status',
            field=models.CharField(choices=[('DIAMOND', 'DIAMOND'), ('SAPPHIRE', 'SAPPHIRE'), ('EMERALD', 'EMERALD'), ('RUBY', 'RUBY')], default='DIAMOND', max_length=10),
        ),
    ]
