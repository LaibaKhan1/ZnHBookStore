# Generated by Django 5.0 on 2024-05-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZnHBookStore', '0003_orders_orderupdate_remove_bookstore_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='book_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]