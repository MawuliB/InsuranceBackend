# Generated by Django 4.0.3 on 2022-05-05 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('motoInsurance', '0002_claim'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_of_driving', models.IntegerField(max_length=4)),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insuranceForm', models.FileField(upload_to='doc/')),
                ('RC_Bood', models.FileField(upload_to='doc/')),
                ('identityProof', models.FileField(upload_to='doc/')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.DeleteModel(
            name='MotoInsurance',
        ),
    ]
