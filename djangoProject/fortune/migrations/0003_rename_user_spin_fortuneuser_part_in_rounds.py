# Generated by Django 4.2.4 on 2023-08-24 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortune', '0002_roulettelog_user_alter_roulettelog_cell_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fortuneuser',
            old_name='user_spin',
            new_name='part_in_rounds',
        ),
    ]
