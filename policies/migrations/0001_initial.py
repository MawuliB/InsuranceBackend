# Generated by Django 4.0.3 on 2022-05-03 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('case_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('case_discription', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PolicyType',
            fields=[
                ('policy_type_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('type_name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=100)),
                ('has_expired', models.BooleanField()),
                ('monthly_payment', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quarterly_payment', models.DecimalField(decimal_places=2, max_digits=20)),
                ('yearly_payment', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_discription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('offer_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('date_signed', models.DateField()),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('terms', models.TextField(max_length=400)),
                ('details', models.TextField(max_length=400)),
                ('is_active', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policies.case')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('policy_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policies.policytype')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policies.products')),
            ],
        ),
    ]
