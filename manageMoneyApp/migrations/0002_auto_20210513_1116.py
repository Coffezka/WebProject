# Generated by Django 3.2 on 2021-05-13 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manageMoneyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersbill',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usersbill',
            name='currencieID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manageMoneyApp.currencie'),
        ),
        migrations.DeleteModel(
            name='billCurrencie',
        ),
    ]
