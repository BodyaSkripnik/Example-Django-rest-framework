# Generated by Django 4.0.5 on 2022-07-15 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_comment_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Culture_and_speed_of_communication',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1),
        ),
        migrations.AddField(
            model_name='comment',
            name='Project_management_level',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1),
        ),
        migrations.AddField(
            model_name='comment',
            name='Quality_of_performance_of_works_services_supplies',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1),
        ),
        migrations.AddField(
            model_name='comment',
            name='Speed_and_quality_of_defect_elimination',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1),
        ),
        migrations.AddField(
            model_name='comment',
            name='Timeliness_of_performance_of_works_services_deliveries',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to='users.participant'),
        ),
    ]
