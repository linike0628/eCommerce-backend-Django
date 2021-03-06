# Generated by Django 2.1.3 on 2020-02-04 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Detail_Customer_After_Delivery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rateorder', models.BooleanField()),
                ('trackpackagelink', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'order_detail_customer_after_delivery',
            },
        ),
        migrations.CreateModel(
            name='Order_Detail_Customer_After_Shipping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('arrivaldate', models.DateField()),
                ('customername', models.CharField(max_length=100)),
                ('itemcost', models.FloatField()),
                ('shippingcost', models.FloatField()),
                ('deliverystatus', models.BooleanField()),
                ('paymentstatus', models.BooleanField()),
                ('paymentmode', models.CharField(choices=[('C', 'Cash'), ('P', 'POS'), ('O', 'Online Payment')], max_length=2)),
                ('trackpackagelink', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'order_detail_customer_after_shipping',
            },
        ),
        migrations.CreateModel(
            name='Order_Detail_Customer_Before_Shipping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estarrivaldate', models.DateField()),
                ('shippingaddress', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('customername', models.CharField(max_length=100)),
                ('itemcost', models.FloatField()),
                ('paymentstatus', models.BooleanField()),
                ('paymentmode', models.CharField(choices=[('C', 'Cash'), ('P', 'POS'), ('O', 'Online Payment')], max_length=2)),
                ('orderdetaillink', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'order_detail_customer_before_shipping',
            },
        ),
        migrations.CreateModel(
            name='Order_Detail_Vendor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orderid', models.CharField(max_length=50)),
                ('productname', models.CharField(max_length=100)),
                ('customername', models.CharField(max_length=100)),
                ('itemcost', models.FloatField()),
                ('paymentstatus', models.BooleanField()),
                ('paymentmode', models.CharField(choices=[('C', 'Cash'), ('P', 'POS'), ('O', 'Online Payment')], max_length=2)),
                ('logistics', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'order_detail_vendor',
            },
        ),
        migrations.AddField(
            model_name='order_detail_customer_before_shipping',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order_Detail_Vendor'),
        ),
        migrations.AddField(
            model_name='order_detail_customer_after_shipping',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order_Detail_Vendor'),
        ),
        migrations.AddField(
            model_name='order_detail_customer_after_delivery',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order_Detail_Vendor'),
        ),
    ]
