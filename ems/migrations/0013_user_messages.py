# Generated by Django 5.0.6 on 2024-07-04 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0012_rename_end_date_leave_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='messages',
            field=models.TextField(blank=True, null=True),
        ),
    ]
