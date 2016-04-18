# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 01:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('annotation', models.TextField()),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='core_annotation_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='core_annotation_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='core_annotation_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='core_annotation_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_core_annotation',
                'abstract': False,
                'verbose_name_plural': 'Annotations',
                'get_latest_by': 'update_time',
                'verbose_name': 'Annotation',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='core_category_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='core_category_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='core_category_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='core_category_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_core_category',
                'abstract': False,
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
                'verbose_name': 'Category',
                'get_latest_by': 'update_time',
            },
        ),
    ]
