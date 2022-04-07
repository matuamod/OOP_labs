# Generated by Django 4.0.3 on 2022-04-01 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_service', '0002_transfer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frozen_acc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_frozen_flag', models.CharField(choices=[('0', '0'), ('1', '1')], max_length=1, verbose_name='Is frozen status')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frozen_account', to='bank_service.account')),
            ],
        ),
    ]