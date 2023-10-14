import os

from espn_api.football import League
from pprint import pprint

env = os.environ
swid = env["SWID"]
espn_s2 = env["S2"]

league = League(league_id=1087311054, year=2023, espn_s2=espn_s2, swid=swid)

# Get teams in the league
teams = [team for team in league.teams]

# Print players on each team
for team in teams:
    print(team)
    players = [player for player in team.roster]
    pprint(players)
