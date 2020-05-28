# Generated by Django 3.0.2 on 2020-01-09 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='street name')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='human name')),
                ('streets_id', models.IntegerField(verbose_name='street name id')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Street')),
            ],
        ),
    ]