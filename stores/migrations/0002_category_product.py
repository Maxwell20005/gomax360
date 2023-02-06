# Generated by Django 4.1.2 on 2022-10-08 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('price', models.PositiveIntegerField()),
                ('discount_price', models.PositiveIntegerField()),
                ('view_count', models.PositiveIntegerField()),
                ('warranty', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='products')),
                ('image_one', models.ImageField(upload_to='products')),
                ('image_two', models.ImageField(upload_to='products')),
                ('image_three', models.ImageField(upload_to='products')),
                ('image_four', models.ImageField(upload_to='products')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.category')),
            ],
        ),
    ]