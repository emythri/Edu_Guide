# Generated by Django 5.1 on 2024-08-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('age', models.CharField(max_length=300, null=True)),
                ('dateofbirth', models.DateTimeField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('category', models.CharField(choices=[('Science', 'Science'), ('Arts', 'Arts')], max_length=300)),
                ('subj', models.ManyToManyField(to='Edu_app.subject')),
            ],
        ),
    ]
