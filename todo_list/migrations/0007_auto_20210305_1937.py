# Generated by Django 3.1.3 on 2021-03-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0006_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stovsuge',
            field=models.CharField(blank=True, choices=[('Ja', 'Ja'), ('Nej', 'Nej')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='vinduer',
            field=models.CharField(blank=True, choices=[('Ja', 'Ja'), ('Nej', 'Nej')], max_length=200, null=True),
        ),
    ]