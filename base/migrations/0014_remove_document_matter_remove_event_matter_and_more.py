# Generated by Django 4.1.6 on 2023-02-12 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_matter_current_lawyer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='matter',
        ),
        migrations.RemoveField(
            model_name='event',
            name='matter',
        ),
        migrations.RemoveField(
            model_name='note',
            name='matter',
        ),
        migrations.RemoveField(
            model_name='task',
            name='matter',
        ),
        migrations.DeleteModel(
            name='Matter',
        ),
    ]