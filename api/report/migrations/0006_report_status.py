# Generated by Django 2.1.7 on 2019-08-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_auto_20190825_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('factchecked', 'Fact Checked'), ('partially_wrong', 'Partially Wrong'), ('wrong', 'Wrong')], default='pending', max_length=128),
        ),
    ]