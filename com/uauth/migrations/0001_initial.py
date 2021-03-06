# Generated by Django 2.2.10 on 2021-08-17 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=30, null=True)),
                ('s_picture', models.ImageField(max_length=255, null=True, upload_to='')),
                ('s_sex', models.CharField(max_length=10, null=True)),
                ('s_certification_type', models.CharField(max_length=20, null=True)),
                ('s_id_number', models.CharField(max_length=30, null=True)),
                ('s_birthday', models.DateTimeField(blank=True, null=True)),
                ('s_politics_status', models.CharField(max_length=30, null=True)),
                ('s_college', models.CharField(max_length=20, null=True)),
                ('s_grade', models.CharField(max_length=20, null=True)),
                ('s_class', models.CharField(max_length=20, null=True)),
                ('s_number', models.CharField(max_length=20, null=True)),
                ('s_mail', models.CharField(max_length=30, null=True)),
                ('s_phone', models.CharField(max_length=20, null=True)),
                ('s_password', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=30, null=True)),
                ('t_picture', models.ImageField(max_length=255, null=True, upload_to='')),
                ('t_sex', models.CharField(max_length=10, null=True)),
                ('t_certification_type', models.CharField(max_length=20, null=True)),
                ('t_id_number', models.CharField(max_length=30, null=True)),
                ('t_birthday', models.DateTimeField(blank=True, null=True)),
                ('t_position', models.CharField(max_length=20, null=True)),
                ('t_college', models.CharField(max_length=20, null=True)),
                ('t_title', models.CharField(max_length=20, null=True)),
                ('t_department', models.CharField(max_length=20, null=True)),
                ('t_number', models.CharField(max_length=20, null=True)),
                ('t_mail', models.CharField(max_length=30, null=True)),
                ('t_phone', models.CharField(max_length=20, null=True)),
                ('t_password', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=30)),
                ('u_phone', models.CharField(max_length=20)),
                ('u_password', models.CharField(max_length=255)),
                ('u_num', models.IntegerField()),
                ('u_ticket', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
