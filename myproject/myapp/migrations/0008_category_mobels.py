# Generated by Django 5.0.3 on 2024-06-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_post_delete_image_remove_phone_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Text', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mobels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebel', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=50)),
                ('is_published', models.BooleanField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='photo=photos/%Y/%n?%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]