# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-31 05:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0034_auto_20171214_1845'),
        ('somno', '0008_auto_20180725_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirwayAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('MouthOpening', models.FloatField(blank=True, null=True)),
                ('Malampati_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('Dentition_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('JawProtusion_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('Dentition_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.Dentition')),
                ('JawProtusion_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.ASA')),
                ('Malampati_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.Malampati')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_somno_airwayassessment_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_somno_airwayassessment_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DrugHistroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('Medications', models.TextField(blank=True, null=True)),
                ('Allergies', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_somno_drughistroy_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_somno_drughistroy_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'verbose_name_plural': 'Diagnoses'},
        ),
        migrations.AlterModelOptions(
            name='investigation',
            options={},
        ),
        migrations.AlterModelOptions(
            name='pastmedicalhistory',
            options={'verbose_name_plural': 'Past medical histories'},
        ),
        migrations.RemoveField(
            model_name='anaestheticassesment',
            name='AdditionalRisks',
        ),
        migrations.RemoveField(
            model_name='anaestheticassesment',
            name='Dentition_fk',
        ),
        migrations.RemoveField(
            model_name='anaestheticassesment',
            name='Dentition_ft',
        ),
        migrations.RemoveField(
            model_name='anaestheticassesment',
            name='General_Risks',
        ),
        migrations.RemoveField(
            model_name='anaestheticassesment',
            name='Malampati_fk',
        ),
        migrations.RemoveField(
            model_name='anaestheticassesment',
            name='Malampati_ft',
        ),
        migrations.AddField(
            model_name='anaestheticassesment',
            name='ExerciseTolerance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anaestheticassesment',
            name='FastingStatus',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anaestheticassesment',
            name='SmokingStatus',
            field=models.TextField(blank=True, null=True),
        ),
    ]
