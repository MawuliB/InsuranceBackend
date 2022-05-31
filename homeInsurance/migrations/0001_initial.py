# Generated by Django 3.0.3 on 2022-05-31 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_form', models.FileField(upload_to='doc/')),
                ('policy_documents', models.FileField(upload_to='doc/')),
                ('chassis_number', models.IntegerField()),
                ('loss_incured', models.DecimalField(decimal_places=2, max_digits=10)),
                ('propertyRateReceipt', models.FileField(upload_to='doc/')),
                ('repair_bill', models.DecimalField(decimal_places=2, max_digits=10)),
                ('surveyor_report', models.FileField(upload_to='doc/')),
                ('police_nonTracable_cet', models.FileField(upload_to='doc/')),
                ('accident_case', models.FileField(upload_to='doc/')),
                ('witness', models.FileField(upload_to='doc/')),
                ('claim_ref', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyDoc', models.FileField(upload_to='doc/')),
                ('buildingType', models.CharField(choices=[('1', 'Detached'), ('2', 'Semi-detached'), ('3', 'Apartement')], default='1', max_length=10)),
                ('noOfStories', models.IntegerField()),
                ('valueOfHome', models.IntegerField()),
                ('valueOfHomePlusItems', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hclient', to='client.Client')),
            ],
        ),
    ]