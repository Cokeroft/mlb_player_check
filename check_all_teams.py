from teams.rosters import *
from main import *


def test_teams():
    target = 'Rays'
    spell_help_list(get_player_list_any('TB'), target)


test_teams()
