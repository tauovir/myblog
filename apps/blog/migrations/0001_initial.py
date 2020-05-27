# Generated by Django 3.0.4 on 2020-05-15 19:07

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brief_summary', ckeditor_uploader.fields.RichTextUploadingField()),
                ('detail_summary', ckeditor_uploader.fields.RichTextUploadingField()),
                ('skils', ckeditor_uploader.fields.RichTextUploadingField()),
                ('blog_summary', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='profiles')),
                ('blog_image', models.ImageField(upload_to='profiles')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post_Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=120)),
                ('image', models.ImageField(null=True, upload_to='subjects')),
                ('status', models.BinaryField(default=1)),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name': 'subscription',
                'verbose_name_plural': 'subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=120)),
                ('summary', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(blank=True, upload_to='blogs')),
                ('banner_image', models.ImageField(null=True, upload_to='banners')),
                ('reference_url', models.URLField(blank=True, default='https://github.com/tauovir')),
                ('code', models.TextField(blank=True, default='')),
                ('output', models.TextField(blank=True, default='')),
                ('code_image', models.ImageField(blank=True, default='', help_text='Coding Image', null=True, upload_to='codes')),
                ('output_image', models.ImageField(blank=True, default='', help_text='Output image', null=True, upload_to='outputs')),
                ('comment_count', models.IntegerField(default=0)),
                ('is_publish', models.IntegerField(choices=[(0, 'Not Publish'), (1, 'Publish')])),
                ('publish_date', models.DateField()),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('post_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post_Subjects')),
            ],
        ),
        migrations.CreateModel(
            name='PostDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('summary', ckeditor_uploader.fields.RichTextUploadingField()),
                ('code', models.TextField(blank=True, default='')),
                ('output', models.TextField(blank=True, default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs')),
                ('code_image', models.ImageField(blank=True, default='', help_text='Coding Image', null=True, upload_to='codes')),
                ('output_image', models.ImageField(blank=True, default='', help_text='Output image', null=True, upload_to='outputs')),
                ('is_publish', models.IntegerField(choices=[(0, 'Not Publish'), (1, 'Publish')])),
                ('publish_date', models.DateTimeField()),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Posts')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('replied_on', models.IntegerField(default=0)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Posts')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
