# Generated by Django 4.0.3 on 2022-05-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motoInsurance', '0004_alter_claim_chassis_number_alter_claim_claim_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationdoc',
            name='years_of_driving',
            field=models.IntegerField(),
        ),
    ]