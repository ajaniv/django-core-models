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
            name='EmailType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_emailtype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_emailtype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_emailtype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_emailtype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_social_media_email_type',
                'abstract': False,
                'verbose_name_plural': 'Email types',
                'ordering': ('name',),
                'verbose_name': 'Email type',
                'get_latest_by': 'update_time',
            },
        ),
        migrations.CreateModel(
            name='FormattedName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_formattedname_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_formattedname_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_formattedname_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_formattedname_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_social_media_formatted_name',
                'abstract': False,
                'verbose_name_plural': 'Formatted names',
                'get_latest_by': 'update_time',
                'verbose_name': 'Formatted name',
            },
        ),
        migrations.CreateModel(
            name='Group',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_group_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_group_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_group_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_group_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_social_media_group',
                'abstract': False,
                'verbose_name_plural': 'Groups',
                'ordering': ('name',),
                'verbose_name': 'Group',
                'get_latest_by': 'update_time',
            },
        ),
        migrations.CreateModel(
            name='InstantMessagingType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessagingtype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessagingtype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessagingtype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessagingtype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_social_media_instant_messaging_type',
                'abstract': False,
                'verbose_name_plural': 'Instant messaging types',
                'ordering': ('name',),
                'verbose_name': 'Instant messaging type',
                'get_latest_by': 'update_time',
            },
        ),
        migrations.CreateModel(
            name='LogoType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_logotype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_logotype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_logotype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_logotype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_social_media_logo_type',
                'abstract': False,
                'verbose_name_plural': 'Logo types',
                'ordering': ('name',),
                'verbose_name': 'Logo type',
                'get_latest_by': 'update_time',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('family_name', models.CharField(max_length=1024)),
                ('given_name', models.CharField(max_length=1024)),
                ('additional_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('honorific_prefix', models.CharField(blank=True, max_length=1024, null=True)),
                ('honorific_suffix', models.CharField(blank=True, max_length=1024, null=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_name_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_name_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_name_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_name_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_social_media_name',
                'abstract': False,
                'verbose_name_plural': 'Names',
                'verbose_name': 'Name',
                'get_latest_by': 'update_time',
            },
        ),
        migrations.CreateModel(
            name='NicknameType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nicknametype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nicknametype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nicknametype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nicknametype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_social_media_nickname_type',
                'abstract': False,
                'verbose_name_plural': 'Nickname types',
                'ordering': ('name',),
                'verbose_name': 'Nickname type',
                'get_latest_by': 'update_time',
            },
        ),
        migrations.CreateModel(
            name='PhoneType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phonetype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phonetype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phonetype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phonetype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_social_media_phone_type',
                'abstract': False,
                'verbose_name_plural': 'Phone types',
                'ordering': ('name',),
                'verbose_name': 'Phone type',
                'get_latest_by': 'update_time',
            },
        ),
        migrations.CreateModel(
            name='PhotoType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phototype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phototype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phototype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phototype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_social_media_photo_type',
                'abstract': False,
                'verbose_name_plural': 'Photo types',
                'ordering': ('name',),
                'verbose_name': 'Photo type',
                'get_latest_by': 'update_time',
            },
        ),
        migrations.CreateModel(
            name='UrlType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_urltype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_urltype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_urltype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_urltype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sl_social_media_url_type',
                'abstract': False,
                'verbose_name_plural': 'Url types',
                'ordering': ('name',),
                'verbose_name': 'Url type',
                'get_latest_by': 'update_time',
            },
        ),
        migrations.AlterUniqueTogether(
            name='name',
            unique_together=set([('family_name', 'given_name', 'additional_name')]),
        ),
    ]