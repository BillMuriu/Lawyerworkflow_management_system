# Generated by Django 4.1.6 on 2023-02-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_alter_document_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
