from teams.rosters import *
from main import *


def test_teams():
    target = 'Pirates'
    spell_help_list(get_player_list_any('PIT'), target)


test_teams()
