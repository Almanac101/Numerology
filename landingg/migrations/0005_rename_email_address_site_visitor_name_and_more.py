# Generated by Django 4.1 on 2022-08-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingg', '0004_rename_alphatable_alphatables'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site_visitor',
            old_name='email_address',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='site_visitor',
            name='first_name',
        ),
        migrations.AddField(
            model_name='site_visitor',
            name='email',
            field=models.EmailField(default='email here', max_length=30),
        ),
    ]
