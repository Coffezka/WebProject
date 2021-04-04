# Generated by Django 3.1.6 on 2021-04-04 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='currencie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
                ('fullName', models.CharField(max_length=30)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='userGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=400)),
                ('dateStart', models.DateTimeField()),
                ('dateEnd', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('goalSum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usersBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=400)),
                ('billName', models.CharField(max_length=30)),
                ('img', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='userSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=400)),
                ('darkTheme', models.BooleanField()),
                ('defaultCurrencie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageMoneyApp.currencie')),
            ],
        ),
        migrations.CreateModel(
            name='userHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=400)),
                ('date', models.DateTimeField()),
                ('function', models.IntegerField()),
                ('category', models.IntegerField()),
                ('sum', models.IntegerField()),
                ('billID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageMoneyApp.usersbill')),
                ('currencieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageMoneyApp.currencie')),
            ],
        ),
        migrations.CreateModel(
            name='billCurrencie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('billID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageMoneyApp.usersbill')),
                ('currencieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageMoneyApp.currencie')),
            ],
        ),
    ]
