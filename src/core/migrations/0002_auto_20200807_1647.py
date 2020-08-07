# Generated by Django 3.1 on 2020-08-07 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biooutput',
            name='num1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='biooutput',
            name='num2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='biooutput',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='biooutput',
            name='other',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='biooutput',
            name='other_thing1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='biooutput',
            name='other_thing2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='biooutput',
            name='protien',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='biooutput',
            name='smile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='biooutput',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='biooutput',
            name='virus',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
