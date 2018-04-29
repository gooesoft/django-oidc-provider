# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-04 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0010_code_is_authentication'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_type',
            field=models.CharField(
                choices=[(b'confidential', b'Confidential'), (b'public', b'Public')],
                default=b'confidential',
                help_text='<b>Confidential</b> clients are capable of maintaining the confidentiality of their '
                          'credentials. <b>Public</b> clients are incapable.',
                max_length=30),
        ),
    ]
