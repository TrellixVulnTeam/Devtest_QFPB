# Generated by Django 3.0.8 on 2020-11-26 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configures',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('name', models.CharField(help_text='配置名称', max_length=50, verbose_name='配置名称')),
                ('author', models.CharField(help_text='编写人员', max_length=50, verbose_name='编写人员')),
                ('request', models.TextField(help_text='请求信息', verbose_name='请求信息')),
                ('interface', models.ForeignKey(help_text='所属接口', on_delete=django.db.models.deletion.CASCADE, related_name='configures', to='interface.Interface_Mo')),
            ],
            options={
                'verbose_name': '配置信息',
                'verbose_name_plural': '配置信息',
                'db_table': 'tb_configures',
            },
        ),
    ]
