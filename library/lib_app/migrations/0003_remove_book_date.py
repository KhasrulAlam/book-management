# Generated by Django 4.1.5 on 2023-05-15 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0002_booktype_book_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date',
        ),
    ]