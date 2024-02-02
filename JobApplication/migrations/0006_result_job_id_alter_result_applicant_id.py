# Generated by Django 4.2.7 on 2024-01-30 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('JobApplication', '0005_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='job_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='JobApplication.job'),
        ),
        migrations.AlterField(
            model_name='result',
            name='applicant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.applicant'),
        ),
    ]
