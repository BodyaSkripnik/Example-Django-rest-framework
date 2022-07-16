# Generated by Django 4.0.5 on 2022-07-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_comment_culture_and_speed_of_communication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Culture_and_speed_of_communication',
            field=models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Project_management_level',
            field=models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Quality_of_performance_of_works_services_supplies',
            field=models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Speed_and_quality_of_defect_elimination',
            field=models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Timeliness_of_performance_of_works_services_deliveries',
            field=models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')]),
        ),
    ]
