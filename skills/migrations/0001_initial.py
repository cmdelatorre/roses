# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seniority',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=256)),
                ('rank', models.IntegerField()),
                ('role', models.ForeignKey(related_name='seniorities', to='skills.Role')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SenioritySkills',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('level', models.CharField(choices=[('none', 'None'), ('low', 'Low'), ('mid', 'Medium'), ('high', 'High'), ('expert', 'Expert')], max_length=256)),
                ('seniority', models.ForeignKey(related_name='skill_levels', to='skills.Seniority')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=1024)),
                ('seniority', models.ManyToManyField(through='skills.SenioritySkills', to='skills.Seniority', related_name='skills')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='seniorityskills',
            name='skill',
            field=models.ForeignKey(related_name='seniority_levels', to='skills.Skill'),
            preserve_default=True,
        ),
    ]
