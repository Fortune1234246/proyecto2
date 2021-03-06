# Generated by Django 2.1.3 on 2018-11-07 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('linea', models.CharField(max_length=60)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('dpi', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='detalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Carro')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('anio_fundacion', models.IntegerField()),
                ('capital', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroVenta', models.IntegerField()),
                ('fecha', models.DateField()),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Cliente')),
                ('detalleVenta', models.ManyToManyField(through='proyecto.detalleVenta', to='proyecto.Carro')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='Venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Venta'),
        ),
        migrations.AddField(
            model_name='carro',
            name='Marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Marca'),
        ),
    ]
