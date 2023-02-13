# Generated by Django 4.1.6 on 2023-02-13 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0019_alter_matter_original_lawyer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientIndividual',
            new_name='IndividualClient',
        ),
        migrations.AddField(
            model_name='matter',
            name='participants',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BusinessClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('primary_phone', models.CharField(max_length=200)),
                ('secondary_phone', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('website', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]