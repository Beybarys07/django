# Generated by Django 5.0.3 on 2024-06-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_luxury_codetmc1_luxury_height1_luxury_length1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='luxury',
            old_name='CodeTMC1',
            new_name='CodeTMC',
        ),
        migrations.AddField(
            model_name='category',
            name='CodeTMC',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
