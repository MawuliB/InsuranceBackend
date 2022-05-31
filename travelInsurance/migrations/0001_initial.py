# Generated by Django 4.0.3 on 2022-05-26 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctry_of_residence', models.CharField(max_length=50)),
                ('passport_number', models.IntegerField()),
                ('destination', models.CharField(max_length=40)),
                ('departure', models.DateField()),
                ('subcription', models.DateField()),
                ('return_date', models.DateField()),
                ('validity', models.DateField()),
                ('druation', models.IntegerField()),
                ('airline', models.CharField(max_length=50)),
                ('port_dpt', models.CharField(max_length=50)),
                ('transit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]