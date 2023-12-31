# Generated by Django 4.2.3 on 2023-07-28 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Doctor_Field', models.CharField(max_length=150)),
                ('Room', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Drug_Stor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_drug', models.CharField(default=None, max_length=100)),
                ('quantity_drugs', models.IntegerField(default=0)),
                ('price_per_drug', models.IntegerField(default=0)),
                ('descriptions_drug', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Prescribe_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescribe_time', models.DateTimeField(auto_now=True)),
                ('prescribe_medication', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.register_patient')),
                ('prescribe_doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.doctors')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_text', models.TextField(max_length=100000000)),
                ('history_time', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.doctors')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.register_patient')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(max_length=700)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.doctors')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.register_patient')),
            ],
        ),
    ]
