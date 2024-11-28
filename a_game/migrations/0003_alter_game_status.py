# Generated by Django 5.1.3 on 2024-11-27 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_game', '0002_game_black_player_game_board_state_game_current_turn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not started'), ('pending', 'Pending'), ('ongoing', 'Ongoing'), ('finished', 'Finished')], default='not_started', max_length=20),
        ),
    ]