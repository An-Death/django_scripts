# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param_table_for_customer', '0011_auto_20171017_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server_connection_info',
            old_name='srv',
            new_name='server',
        ),
    ]