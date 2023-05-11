from teams.rosters import *
from main import *


def test_teams():
    target = 'Cubs'
    spell_help_list(get_player_list_any('ARI'), target)


test_teams()
