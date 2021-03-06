# Generated by Django 3.0.4 on 2020-06-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200602_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post_subjects',
            options={'verbose_name': 'post_subject', 'verbose_name_plural': 'post_subjects'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AlterField(
            model_name='post_subjects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subjects'),
        ),
    ]
