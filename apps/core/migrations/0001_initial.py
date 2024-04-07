# Generated by Django 4.2.6 on 2024-03-09 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('bn_name', models.CharField(blank=True, max_length=250, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('long', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('bn_name', models.CharField(blank=True, max_length=250, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('long', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('bn_name', models.CharField(blank=True, max_length=250, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('long', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upazila', to='core.district')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('upazila', models.CharField(blank=True, max_length=250, null=True)),
                ('postOffice', models.CharField(blank=True, max_length=250, null=True)),
                ('postCode', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.district')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.division')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district', to='core.division'),
        ),
    ]
