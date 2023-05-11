import requests
import datetime

# AL Teams
la_angels, hou_astros, oak_athletics, sea_mariners, tex_rangers = '108', '117', '133', '136', '140'
bal_orioles, bos_redsox, ny_yankees, tb_rays, tor_bluejays = '110', '111', '147', '139', '141'
cle_guardians, det_tigers, kc_royals, chi_whitesox, min_twins = '114', '116', '118', '145', '142'
# NL Teams
chi_cubs, cin_reds, mil_brewers, pitt_pirates, stl_cardinals = '112', '113', '158', '134', '138'
ari_dbacks, col_rockies, la_dodgers, sd_padres, sf_giants = '109', '115', '119', '135', '137'
was_nationals, ny_mets, atl_braves, mia_marlins, phi_phillies = '120', '121', '144', '146', '143'


def get_player_list_any(team_name):
    team_data = get_teams_list()
    team_id = ''
    for x in range(len(team_data)):
        if team_data[x]['bis_team_code'] == team_name:
            team_id = team_data[x]['mlb_org_id']

    if team_id == '':
        print("That team doesn't exist!")
        exit()

    player_list = list()
    response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id='{team_id}'")
    response_json = response.json()
    response_rows = response_json['roster_40']['queryResults']['row']
    for x in range(len(response_rows)):
        player_list.append(response_rows[x]['name_display_first_last'])
    return player_list


def get_player_list_chc():
    player_list_chc = list()
    response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id='{chi_cubs}'")
    response_json = response.json()
    response_rows = response_json['roster_40']['queryResults']['row']
    for x in range(len(response_rows)):
        player_list_chc.append(response_rows[x]['name_display_first_last'])
    return player_list_chc


def get_teams_list():
    today = datetime.datetime.today()
    current_year = today.year
    response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?"
                            f"sport_code='mlb'&all_star_sw='N'&sort_order=name_asc&season='{current_year}'")
    response_json = response.json()
    response_rows = response_json['team_all_season']['queryResults']['row']
    return response_rows

