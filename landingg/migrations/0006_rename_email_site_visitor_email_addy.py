# Generated by Django 4.1 on 2022-08-24 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingg', '0005_rename_email_address_site_visitor_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site_visitor',
            old_name='email',
            new_name='email_addy',
        ),
    ]
