# Generated by Django 4.2.16 on 2024-11-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=30, verbose_name='项目名称')),
                ('project_type', models.CharField(max_length=30, verbose_name='项目类型')),
                ('project_desc', models.TextField(verbose_name='项目描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '项目表',
                'verbose_name_plural': '项目表',
                'db_table': 'Auto_project_info',
                'ordering': ['project_id'],
            },
        ),
    ]
