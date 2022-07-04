# Generated by Django 4.0.5 on 2022-07-04 15:53

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0003_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=10, max_length=13, prefix='id_', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=150, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Comentss',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=10, max_length=13, prefix='id_', primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to='users.participant')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projects.project')),
            ],
        ),
    ]