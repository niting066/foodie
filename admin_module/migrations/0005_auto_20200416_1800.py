# Generated by Django 3.0 on 2020-04-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0004_auto_20200416_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areamodel',
            name='area_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
