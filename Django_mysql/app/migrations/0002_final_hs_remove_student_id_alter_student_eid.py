# Generated by Django 4.2.2 on 2023-07-09 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Final_HS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('eid', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=50)),
                ('Course', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Final_HS',
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='eid',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
