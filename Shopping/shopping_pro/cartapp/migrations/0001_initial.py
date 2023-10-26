# Generated by Django 4.2.6 on 2023-10-21 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopping_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cart',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='cartitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapp.cart')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_app.product')),
            ],
            options={
                'db_table': 'cartitem',
            },
        ),
    ]