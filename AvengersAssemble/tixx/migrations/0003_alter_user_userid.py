# Generated by Django 5.0.3 on 2024-03-28 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tixx', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]