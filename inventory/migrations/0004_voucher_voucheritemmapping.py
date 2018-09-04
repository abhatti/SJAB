# Generated by Django 2.0.6 on 2018-08-30 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20180829_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_number', models.BigIntegerField(auto_created=True, unique=True)),
                ('issued_by', models.CharField(max_length=30)),
                ('issued_to', models.CharField(max_length=30)),
                ('date_issued', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoucherItemMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Category')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
                ('voucher_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Voucher')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Warehouse')),
            ],
        ),
    ]