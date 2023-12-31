# Generated by Django 4.2.2 on 2023-06-21 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cpopulation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital_name', models.CharField(max_length=20)),
                ('capital_population', models.IntegerField()),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]
