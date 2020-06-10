# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    name = models.CharField(unique=True, max_length=100)
    distance = models.FloatField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    category_fk = models.ForeignKey('Category', models.DO_NOTHING, db_column='category_fk')

    class Meta:
        managed = False
        db_table = 'activity'


class Category(models.Model):
    name = models.CharField(max_length=100)
    weekly_goal = models.IntegerField(blank=True, null=True)
    metacat_fk = models.ForeignKey('MetaCategory', models.DO_NOTHING, db_column='metacat_fk')

    class Meta:
        managed = False
        db_table = 'category'


class FitActivity(models.Model):
    calories = models.FloatField(blank=True, null=True)
    heart_rate = models.IntegerField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    activity_fk = models.OneToOneField(Activity, models.DO_NOTHING, db_column='activity_fk')
    pace = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fit_activity'


class MetaCategory(models.Model):
    name = models.CharField(max_length=100)
    weekly_goal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_category'
