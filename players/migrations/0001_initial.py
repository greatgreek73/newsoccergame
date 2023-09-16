# Generated by Django 4.2.3 on 2023-08-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('position', models.CharField(choices=[('Goalkeeper', 'Goalkeeper'), ('Defender Center', 'Defender Center'), ('Defender Left', 'Defender Left'), ('Defender Right', 'Defender Right'), ('Defensive Midfielder Center', 'Defensive Midfielder Center'), ('Defensive Midfielder Left', 'Defensive Midfielder Left'), ('Defensive Midfielder Right', 'Defensive Midfielder Right'), ('Midfielder Left', 'Midfielder Left'), ('Midfielder Center', 'Midfielder Center'), ('Midfielder Right', 'Midfielder Right'), ('Offensive Midfielder Left', 'Offensive Midfielder Left'), ('Offensive Midfielder Center', 'Offensive Midfielder Center'), ('Offensive Midfielder Right', 'Offensive Midfielder Right'), ('Forward', 'Forward')], max_length=50)),
                ('strength', models.IntegerField()),
                ('stamina', models.IntegerField()),
                ('pace', models.IntegerField()),
                ('marking', models.IntegerField(blank=True, null=True)),
                ('tackling', models.IntegerField(blank=True, null=True)),
                ('work_rate', models.IntegerField(blank=True, null=True)),
                ('positioning', models.IntegerField(blank=True, null=True)),
                ('passing', models.IntegerField(blank=True, null=True)),
                ('crossing', models.IntegerField(blank=True, null=True)),
                ('technique', models.IntegerField(blank=True, null=True)),
                ('heading', models.IntegerField(blank=True, null=True)),
                ('finishing', models.IntegerField(blank=True, null=True)),
                ('long_shots', models.IntegerField(blank=True, null=True)),
                ('set_pieces', models.IntegerField(blank=True, null=True)),
                ('handling', models.IntegerField(blank=True, null=True)),
                ('one_on_ones', models.IntegerField(blank=True, null=True)),
                ('reflexes', models.IntegerField(blank=True, null=True)),
                ('aerial', models.IntegerField(blank=True, null=True)),
                ('jumping', models.IntegerField(blank=True, null=True)),
                ('communication', models.IntegerField(blank=True, null=True)),
                ('throwing', models.IntegerField(blank=True, null=True)),
                ('kicking', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]