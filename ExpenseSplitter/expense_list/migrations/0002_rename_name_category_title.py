# Generated by Django 4.1.3 on 2022-11-09 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
    ]