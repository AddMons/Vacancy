# Generated by Django 3.1.1 on 2020-12-03 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vacancies', '0002_auto_20201202_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='icon',
            field=models.ImageField(upload_to='Vacancies/static/img'),
        ),
    ]