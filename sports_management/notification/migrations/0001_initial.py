# Generated by Django 3.2.15 on 2023-02-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('notification', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'notification',
                'managed': False,
            },
        ),
    ]
