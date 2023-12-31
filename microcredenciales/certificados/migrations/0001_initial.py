# Generated by Django 4.2.6 on 2023-10-11 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Microcredencial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('contenido_IPFS', models.CharField(max_length=255)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificados.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('microcredencial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificados.microcredencial')),
            ],
        ),
        migrations.AddField(
            model_name='microcredencial',
            name='universidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificados.universidad'),
        ),
    ]
