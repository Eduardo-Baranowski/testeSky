# Generated by Django 2.2.10 on 2020-11-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createPaper', '0004_paper_data_ligacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperitemassociado',
            name='obs',
            field=models.TextField(default='', verbose_name='obs'),
        ),
    ]
