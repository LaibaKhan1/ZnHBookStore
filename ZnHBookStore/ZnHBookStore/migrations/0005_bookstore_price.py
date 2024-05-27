# Generated by Django 5.0 on 2024-05-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZnHBookStore', '0004_alter_bookstore_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstore',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
