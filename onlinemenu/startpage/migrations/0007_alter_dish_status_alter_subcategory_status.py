# Generated by Django 4.0.5 on 2022-09-16 10:29

from django.db import migrations, models
import startpage.models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0006_alter_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='status',
            field=models.CharField(choices=[('Active', startpage.models.Dish.Status['Active']), ('Deleted', startpage.models.Dish.Status['Deleted']), ('Inactive', startpage.models.Dish.Status['Inactive'])], default=startpage.models.Dish.Status['Active'], max_length=100),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='status',
            field=models.CharField(choices=[('Active', startpage.models.SubCategory.Status['Active']), ('Deleted', startpage.models.SubCategory.Status['Deleted']), ('Inactive', startpage.models.SubCategory.Status['Inactive'])], default=startpage.models.SubCategory.Status['Active'], max_length=100),
        ),
    ]
