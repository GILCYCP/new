# Generated by Django 3.2.15 on 2023-02-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_id', models.AutoField(primary_key=True, serialize=False)),
                ('club_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=45)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'club',
                'managed': False,
            },
        ),
    ]
