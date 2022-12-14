# Generated by Django 4.0.5 on 2022-09-16 08:22

from django.db import migrations, models
import django.db.models.deletion
import startpage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modifield_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[(startpage.models.Category.Status['Active'], 'Active'), (startpage.models.Category.Status['Deleted'], 'Deleted'), (startpage.models.Category.Status['Inactive'], 'Inactive')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modifield_at', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='startpage.category')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('images', models.ImageField(null=True, upload_to='images')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modifield_at', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='startpage.category')),
                ('subcat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='startpage.subcategory')),
            ],
        ),
    ]
