# Generated by Django 2.1.5 on 2019-10-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_auto_20191012_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='HDD_Disposed',
            field=models.BooleanField(choices=[('Yes', True), ('No', False)], default='Yes'),
        ),
    ]
