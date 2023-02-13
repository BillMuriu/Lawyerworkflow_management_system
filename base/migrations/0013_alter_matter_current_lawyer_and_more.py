# Generated by Django 4.1.6 on 2023-02-12 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_rename_paralegal_lawyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matter',
            name='current_lawyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_lawyer', to='base.lawyer'),
        ),
        migrations.AlterField(
            model_name='matter',
            name='original_lawyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_lawyer', to='base.lawyer'),
        ),
    ]