# Generated by Django 4.1.2 on 2022-10-17 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_profile_pix_profile_profile_picture'),
        ('stores', '0017_alter_product_discount_price_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_address', models.TextField()),
                ('order_by', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('discount', models.PositiveIntegerField()),
                ('subtotal', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('order_status', models.CharField(choices=[('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('Order Shipped out', 'Order Shipped out'), ('Order Canceled', 'Order Canceled'), ('Order Completed', 'Order Completed')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stores.cart')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('subtotal', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.product')),
            ],
        ),
    ]
