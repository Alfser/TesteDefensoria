# Generated by Django 4.0.5 on 2022-06-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleform', '0002_alter_person_adress_alter_person_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(help_text='Informe o seu nome completo', max_length=255, verbose_name='Nome Completo'),
        ),
    ]
