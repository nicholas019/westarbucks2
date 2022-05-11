# Generated by Django 4.0.4 on 2022-05-11 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=45)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
            ],
            options={
                'db_table': 'categories',
            },
        ),
    ]
