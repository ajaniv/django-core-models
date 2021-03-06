# Generated by Django 2.1.1 on 2018-09-14 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_core_utils.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('address', models.EmailField(max_length=254, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_email_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_email_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_email_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_email_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
                'db_table': 'sl_social_media_email',
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
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
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_emailtype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_emailtype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_emailtype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_emailtype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Email type',
                'verbose_name_plural': 'Email types',
                'db_table': 'sl_social_media_email_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
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
                ('name', models.CharField(max_length=1024)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_formattedname_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_formattedname_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_formattedname_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_formattedname_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Formatted name',
                'verbose_name_plural': 'Formatted names',
                'db_table': 'sl_social_media_formatted_name',
                'get_latest_by': 'update_time',
                'abstract': False,
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
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_group_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_group_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_group_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_group_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'db_table': 'sl_social_media_group',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstantMessaging',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('address', django_core_utils.fields.InstantMessagingField(unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessaging_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessaging_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessaging_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessaging_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Instant messaging',
                'verbose_name_plural': 'Instant messagings',
                'db_table': 'sl_social_media_instant_messaging',
                'get_latest_by': 'update_time',
                'abstract': False,
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
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessagingtype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessagingtype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessagingtype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_instantmessagingtype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Instant messaging type',
                'verbose_name_plural': 'Instant messaging types',
                'db_table': 'sl_social_media_instant_messaging_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
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
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_logotype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_logotype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_logotype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_logotype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Logo type',
                'verbose_name_plural': 'Logo types',
                'db_table': 'sl_social_media_logo_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
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
                ('family_name', models.CharField(max_length=255)),
                ('given_name', models.CharField(max_length=255)),
                ('additional_name', models.CharField(blank=True, max_length=255, null=True)),
                ('honorific_prefix', models.CharField(blank=True, max_length=1024, null=True)),
                ('honorific_suffix', models.CharField(blank=True, max_length=1024, null=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_name_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_name_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_name_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_name_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Name',
                'verbose_name_plural': 'Names',
                'db_table': 'sl_social_media_name',
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nickname',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nickname_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nickname_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nickname_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nickname_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Nickname',
                'verbose_name_plural': 'Nicknames',
                'db_table': 'sl_social_media_nickname',
                'get_latest_by': 'update_time',
                'abstract': False,
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
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nicknametype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nicknametype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nicknametype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_nicknametype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Nickname type',
                'verbose_name_plural': 'Nickname types',
                'db_table': 'sl_social_media_nickname_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phone_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phone_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phone_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phone_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phones',
                'db_table': 'sl_social_media_phone',
                'get_latest_by': 'update_time',
                'abstract': False,
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
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phonetype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phonetype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phonetype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phonetype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Phone type',
                'verbose_name_plural': 'Phone types',
                'db_table': 'sl_social_media_phone_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
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
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phototype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phototype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phototype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_phototype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Photo type',
                'verbose_name_plural': 'Photo types',
                'db_table': 'sl_social_media_photo_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('address', models.URLField(max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_url_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_url_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_url_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_url_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Url',
                'verbose_name_plural': 'Urls',
                'db_table': 'sl_social_media_url',
                'get_latest_by': 'update_time',
                'abstract': False,
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
                ('alias', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_urltype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_urltype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_urltype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_media_urltype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Url type',
                'verbose_name_plural': 'Url types',
                'db_table': 'sl_social_media_url_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='name',
            unique_together={('family_name', 'given_name', 'additional_name')},
        ),
    ]
