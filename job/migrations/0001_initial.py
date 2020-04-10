# Generated by Django 2.2.4 on 2020-04-10 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('company', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('how_to_a', models.CharField(max_length=250)),
                ('deadline', models.DateTimeField()),
                ('image', models.ImageField(upload_to='jobs/images/')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('poster', models.CharField(default='blogsmond', max_length=25)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=250)),
                ('course', models.CharField(max_length=250)),
                ('requirement', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('benefit', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('how_to_a', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='scholarships/images/')),
                ('deadline', models.DateTimeField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('poster', models.CharField(default='blogsmond', max_length=25)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
