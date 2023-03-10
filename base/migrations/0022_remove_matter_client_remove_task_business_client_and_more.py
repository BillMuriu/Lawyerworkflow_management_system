# Generated by Django 4.1.6 on 2023-02-13 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_task_business_client_task_individual_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matter',
            name='client',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Business_client',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Individual_client',
        ),
        migrations.AddField(
            model_name='matter',
            name='business_client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.businessclient'),
        ),
        migrations.AddField(
            model_name='matter',
            name='individual_clients',
            field=models.ManyToManyField(blank=True, to='base.individualclient'),
        ),
    ]
