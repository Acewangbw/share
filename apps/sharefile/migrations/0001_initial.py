# Generated by Django 2.0 on 2019-01-16 11:23

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('models_Filename', models.CharField(default='', max_length=20, verbose_name='文件名称')),
                ('models_Filedepartment', models.CharField(default='', max_length=20, verbose_name='BUH')),
                ('models_Filedes', models.TextField(default='', verbose_name='描述')),
                ('models_Fileusedfor', models.CharField(default='', max_length=20, verbose_name='人数')),
                ('models_Fileupload', models.FileField(max_length=1000, upload_to='file/%Y/%m', verbose_name='文件')),
                ('models_Updated_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('models_clicknum', models.IntegerField(default=0, verbose_name='下载次数')),
            ],
            options={
                'verbose_name': '上传文件',
                'verbose_name_plural': '上传文件',
            },
        ),
        migrations.CreateModel(
            name='DayNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now, verbose_name='日期')),
                ('count', models.IntegerField(default=0, verbose_name='网站访问次数')),
            ],
            options={
                'verbose_name': '网站日访问量统计',
                'verbose_name_plural': '网站日访问量统计',
            },
        ),
        migrations.CreateModel(
            name='FileUsedfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usedfor', models.CharField(max_length=20, verbose_name='用于')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Userip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='IP地址')),
                ('count', models.IntegerField(default=0, verbose_name='访问次数')),
            ],
            options={
                'verbose_name': '访问用户信息',
                'verbose_name_plural': '访问用户信息',
            },
        ),
        migrations.CreateModel(
            name='VisitNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='网站访问总次数')),
            ],
            options={
                'verbose_name': '网站访问总次数',
                'verbose_name_plural': '网站访问总次数',
            },
        ),
    ]
