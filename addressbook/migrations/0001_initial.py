# Generated by Django 2.2.7 on 2019-12-07 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('citizens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village', models.CharField(max_length=100)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.Cell')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.District')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.Province'),
        ),
        migrations.AddField(
            model_name='cell',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.Sector'),
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=50)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.Cell')),
                ('citizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citizens.Citizen')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.District')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.Province')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.Sector')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.Village')),
            ],
        ),
    ]