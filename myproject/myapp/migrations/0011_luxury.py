# Generated by Django 5.0.3 on 2024-06-18 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_category_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Luxury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name1', models.CharField(max_length=100)),
                ('Text1', models.CharField(max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.category')),
            ],
        ),
    ]
