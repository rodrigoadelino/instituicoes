# Generated by Django 4.2.1 on 2023-06-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='numero_codigo',
            field=models.CharField(blank=True, default='', max_length=4, null=True),
        ),
    ]
