# Generated by Django 4.1.6 on 2023-02-13 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_remove_matter_client_remove_task_business_client_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matter',
            old_name='individual_clients',
            new_name='individual_client',
        ),
    ]
