# Generated by Django 3.2.7 on 2021-09-29 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210929_0647'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactMessage',
        ),
    ]
