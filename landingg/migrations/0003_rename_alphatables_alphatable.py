# Generated by Django 4.1 on 2022-08-14 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingg', '0002_alphaguide_delete_letter_attributes_alphatables'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alphatables',
            new_name='Alphatable',
        ),
    ]