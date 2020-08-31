# Generated by Django 3.1 on 2020-08-29 16:39

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, default='/static/img/900x300.png', upload_to='images/')),
                ('slug', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Excerpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excerpt', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.blogcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]