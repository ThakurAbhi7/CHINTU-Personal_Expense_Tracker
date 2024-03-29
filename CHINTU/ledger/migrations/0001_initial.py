# Generated by Django 2.2.6 on 2019-10-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_auto_20191025_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('own', models.CharField(max_length=40)),
                ('amount', models.FloatField()),
                ('owned', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('category', models.CharField(max_length=100)),
                ('bill', models.FilePathField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=40)),
                ('participants', models.ManyToManyField(to='account.User')),
            ],
        ),
    ]
