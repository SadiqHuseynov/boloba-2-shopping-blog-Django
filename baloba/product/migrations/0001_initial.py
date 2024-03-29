# Generated by Django 4.2.6 on 2023-11-26 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Maximum 100 characters', max_length=100, verbose_name='Name of product')),
                ('star', models.IntegerField(verbose_name='Star of product')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value of product')),
                ('description', models.TextField(blank=True, verbose_name='Description of product')),
                ('brand', models.CharField(help_text='Maximum 50 characters', max_length=50, verbose_name='Brand')),
                ('product_code', models.CharField(help_text='Maximum 20 characters', max_length=20, verbose_name='Product Code')),
                ('reward_points', models.IntegerField(verbose_name='Reward Points of product')),
                ('availability', models.BooleanField(default=True, verbose_name='Availability of product')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'All Product',
            },
        ),
    ]
