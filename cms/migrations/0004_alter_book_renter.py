# Generated by Django 4.0.4 on 2022-04-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_book_book_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='renter',
            field=models.CharField(blank=True, max_length=64, verbose_name='借りている人'),
        ),
    ]