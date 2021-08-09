# Generated by Django 3.2.6 on 2021-08-06 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('amount', models.IntegerField()),
                ('stage', models.CharField(choices=[('D', 'Discovery'), ('P', 'Proposal Shared'), ('N', 'Negotiations')], max_length=50)),
                ('assoc_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='accounts.account')),
            ],
            options={
                'verbose_name_plural': 'Opportunities',
            },
        ),
    ]
