# Generated by Django 3.2.15 on 2023-02-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=35)),
                ('game_points', models.IntegerField()),
            ],
            options={
                'db_table': 'games',
                'managed': False,
            },
        ),
    ]
