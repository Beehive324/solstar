# Generated by Django 4.2.5 on 2023-09-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solstar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
