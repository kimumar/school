# Generated by Django 3.2.7 on 2021-09-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_contact_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]