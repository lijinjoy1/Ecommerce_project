# Generated by Django 3.2.7 on 2021-09-27 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='uploads/products/'),
        ),
    ]