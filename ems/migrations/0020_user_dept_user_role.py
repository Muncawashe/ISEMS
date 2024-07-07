# Generated by Django 5.0.6 on 2024-07-07 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0019_remove_user_dept_remove_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dept',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dept', to='ems.department'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='ems.role'),
        ),
    ]
