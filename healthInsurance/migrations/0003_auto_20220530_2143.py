# Generated by Django 3.0.3 on 2022-05-30 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthInsurance', '0002_alter_applicationdoc_voting_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationdoc',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]