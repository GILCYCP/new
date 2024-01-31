# Generated by Django 3.2.15 on 2023-02-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('sportsitem_name', models.CharField(max_length=35)),
                ('amount', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
    ]