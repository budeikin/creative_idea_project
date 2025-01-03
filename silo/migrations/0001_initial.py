# Generated by Django 3.2 on 2024-12-27 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Silo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField()),
                ('current_stock', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SiloLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_type', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('silo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='silo.silo')),
            ],
        ),
    ]
