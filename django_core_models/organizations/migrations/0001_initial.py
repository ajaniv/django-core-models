# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 00:19
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('uri', models.URLField(blank=True, max_length=255, null=True, validators=[django.core.validators.URLValidator(schemes=['aim', 'gtalk', 'im', 'msnim', 'skype', 'sms', 'xmpp', 'http', 'https', 'ftp', 'ftps', 'tel', 'mailto', 'urn'])])),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organization_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organization_related_effective_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'verbose_name_plural': 'Organizations',
                'verbose_name': 'Organization',
                'db_table': 'sl_organizations_organization',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organizationtype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organizationtype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organizationtype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organizationtype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'verbose_name_plural': 'Organization types',
                'verbose_name': 'Organization type',
                'db_table': 'sl_organizations_organization_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organizationunit_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organizationunit_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizations.Organization')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organizationunit_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organizationunit_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'verbose_name_plural': 'Organization units',
                'verbose_name': 'Organization unit',
                'db_table': 'sl_organizations_organization_unit',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_role_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_role_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_role_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_role_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'verbose_name_plural': 'Roles',
                'verbose_name': 'Role',
                'db_table': 'sl_organizations_role',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_title_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_title_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_title_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_title_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'verbose_name_plural': 'Titles',
                'verbose_name': 'Title',
                'db_table': 'sl_organizations_title',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='organization_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizations.OrganizationType'),
        ),
        migrations.AddField(
            model_name='organization',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organization_related_site', to='sites.Site'),
        ),
        migrations.AddField(
            model_name='organization',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations_organization_related_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='organization',
            unique_together=set([('name', 'organization_type')]),
        ),
    ]
