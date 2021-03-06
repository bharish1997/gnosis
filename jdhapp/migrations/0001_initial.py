# Generated by Django 2.2 on 2020-05-10 17:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Z_]*$', 'Only uppercase letters and underscores allowed.')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Z_]*$', 'Only uppercase letters and underscores allowed.')])),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=10)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Z_]*$', 'Only uppercase letters and underscores allowed.')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Z_]*$', 'Only uppercase letters and underscores allowed.')])),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=10)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('video', models.FileField(upload_to='video/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='jdhapp.Category')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_creator', to='jdhapp.Instructor')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
