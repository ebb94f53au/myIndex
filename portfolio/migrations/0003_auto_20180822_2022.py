# Generated by Django 2.0.7 on 2018-08-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20180818_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project',
            field=models.FileField(default='images/portfolio/file/null', upload_to='images/portfolio/file', verbose_name='项目*'),
        ),
    ]
