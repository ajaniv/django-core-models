# Generated by Django 2.1.1 on 2018-09-14 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_core_utils.fields
import timezone_field.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(blank=True, max_length=1024, null=True)),
                ('post_office_box', models.CharField(blank=True, max_length=32, null=True)),
                ('street_address', models.CharField(blank=True, max_length=196, null=True)),
                ('extended_address', models.CharField(blank=True, max_length=196, null=True)),
                ('city', models.CharField(max_length=128)),
                ('postal_code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'db_table': 'sl_locations_address',
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AddressType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_addresstype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_addresstype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_addresstype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_addresstype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address type',
                'verbose_name_plural': 'Address types',
                'db_table': 'sl_locations_address_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_city_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_city_related_effective_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'sl_locations_city',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
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
                ('iso_code', models.CharField(max_length=2, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_country_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_country_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_country_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_country_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'sl_locations_country',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DistanceUnit',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_distanceunit_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_distanceunit_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_distanceunit_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_distanceunit_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Distance unit',
                'verbose_name_plural': 'Distance units',
                'db_table': 'sl_locations_distance_unit',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeographicLocation',
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
                ('name', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, default=None, max_digits=9, validators=[django_core_utils.fields.latitude_validator])),
                ('longitude', models.DecimalField(decimal_places=6, default=None, max_digits=9, validators=[django_core_utils.fields.longitude_validator])),
                ('range', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_geographiclocation_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_geographiclocation_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('range_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.DistanceUnit')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_geographiclocation_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_geographiclocation_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Geographic location',
                'verbose_name_plural': 'Geographic locations',
                'db_table': 'sl_locations_geographic_location',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeographicLocationType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_geographiclocationtype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_geographiclocationtype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_geographiclocationtype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_geographiclocationtype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Geographic location type',
                'verbose_name_plural': 'Geographic location types',
                'db_table': 'sl_locations_geographic_location_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
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
                ('iso_code', models.CharField(max_length=2, unique=True)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_language_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_language_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_language_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_language_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'db_table': 'sl_locations_language',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LanguageType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_languagetype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_languagetype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_languagetype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_languagetype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Language type',
                'verbose_name_plural': 'Language types',
                'db_table': 'sl_locations_language_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Province',
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
                ('iso_code', models.CharField(max_length=6, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.Country')),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_province_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_province_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_province_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_province_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
                'db_table': 'sl_locations_province',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
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
                ('iso_code', models.CharField(max_length=6, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.Country')),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_state_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_state_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_state_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_state_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
                'db_table': 'sl_locations_state',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Timezone',
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
                ('name', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('timezone', timezone_field.fields.TimeZoneField(default='America/New_York')),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_timezone_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_timezone_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_timezone_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_timezone_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Timezone',
                'verbose_name_plural': 'Timezones',
                'db_table': 'sl_locations_timezone',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimezoneType',
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
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_timezonetype_related_creation_user', to=settings.AUTH_USER_MODEL)),
                ('effective_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_timezonetype_related_effective_user', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_timezonetype_related_site', to='sites.Site')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_timezonetype_related_update_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Timezone type',
                'verbose_name_plural': 'Timezone types',
                'db_table': 'sl_locations_timezone_type',
                'ordering': ('name',),
                'get_latest_by': 'update_time',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.Province'),
        ),
        migrations.AddField(
            model_name='city',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_city_related_site', to='sites.Site'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.State'),
        ),
        migrations.AddField(
            model_name='city',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_city_related_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.Country'),
        ),
        migrations.AddField(
            model_name='address',
            name='creation_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_address_related_creation_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='effective_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_address_related_effective_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='geographic_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.GeographicLocation'),
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.Province'),
        ),
        migrations.AddField(
            model_name='address',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_address_related_site', to='sites.Site'),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.State'),
        ),
        migrations.AddField(
            model_name='address',
            name='timezone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.Timezone'),
        ),
        migrations.AddField(
            model_name='address',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_address_related_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('street_address', 'city', 'postal_code', 'country', 'state', 'province', 'extended_address', 'post_office_box')},
        ),
    ]
