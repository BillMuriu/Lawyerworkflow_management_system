# Generated by Django 4.1.6 on 2023-03-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_document_file_alter_document_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]