# Generated by Django 3.0.4 on 2020-05-15 19:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default='', max_length=120)),
                ('employer', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120, null=True)),
                ('summary', models.TextField(max_length=800)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_current_org', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language_Proficiency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('is_other', models.IntegerField(choices=[(1, 'Active'), (0, 'Not Active')], default=1)),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=120)),
                ('middle_name', models.CharField(default='', max_length=120)),
                ('last_name', models.CharField(default='', max_length=120)),
                ('profile_title', models.CharField(default='', max_length=120)),
                ('brief_summary', models.TextField(default='', max_length=800)),
                ('email', models.EmailField(default='', max_length=50)),
                ('mobile_number', models.CharField(default='', max_length=15)),
                ('profile_pic', models.ImageField(upload_to='profile')),
                ('banner_image', models.ImageField(upload_to='profile')),
                ('social_linkes', models.CharField(default='', max_length=250)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technology_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Not Active')], default=1)),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='User_Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Languages')),
                ('language_profiency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Language_Proficiency')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='User_Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('version', models.CharField(blank=True, default='', max_length=120)),
                ('rate', models.SmallIntegerField(default=70)),
                ('is_other', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Technology_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=800)),
                ('role_responsibility', models.TextField(max_length=300)),
                ('team_size', models.PositiveSmallIntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('employment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Employment')),
                ('technology', models.ManyToManyField(to='portfolio.Technologies')),
            ],
        ),
        migrations.AddField(
            model_name='employment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Profile'),
        ),
        migrations.CreateModel(
            name='Educations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_short_name', models.CharField(max_length=100, null=True)),
                ('course_full_name', models.CharField(max_length=100, null=True)),
                ('institute_short_name', models.CharField(max_length=50, null=True)),
                ('institute_full_name', models.CharField(max_length=100, null=True)),
                ('university', models.CharField(max_length=100, null=True)),
                ('start_year', models.PositiveSmallIntegerField()),
                ('end_year', models.PositiveSmallIntegerField()),
                ('duration', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('is_school', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('short_name', models.CharField(max_length=100, null=True)),
                ('institute_short_name', models.CharField(max_length=50, null=True)),
                ('institute_full_name', models.CharField(max_length=100, null=True)),
                ('complition_date', models.DateField()),
                ('duration', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Profile')),
            ],
        ),
    ]
