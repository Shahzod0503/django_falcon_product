# Generated by Django 4.1.3 on 2022-12-09 12:37

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, verbose_name=models.CharField(max_length=255))),
            ],
            options={
                'db_table': 'Categorys',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('teg', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('price', models.DecimalField(decimal_places=1, max_digits=9)),
                ('discount', models.ImageField(default=0, upload_to='')),
                ('rating', models.IntegerField(choices=[(1, 'Worse'), (2, 'Bad'), (3, 'Average'), (4, 'Got'), (5, 'Excellent')], default=3)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created', to=settings.AUTH_USER_MODEL)),
                ('updated_at', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated', to=settings.AUTH_USER_MODEL)),
                ('wishlist', models.ManyToManyField(related_name='wishlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'products',
                'ordering': ('-created_at',),
            },
        ),
    ]