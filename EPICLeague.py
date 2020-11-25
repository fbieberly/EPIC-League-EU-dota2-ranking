from glicko2 import Glicko2

def compute_series(team_dict, series):
    '''
    Enter the results of a series. The rankings are updated and stored in the dictionary
    example: compute_series(team_dictionary, [og, liquid, [1, 0, 1]])
        For a series where OG beats liquid 2-1 (winning the first and last map)

    '''
    team1 = series[0]
    team2 = series[1]
    games = series[2]

    for game in games:
        if game == 1:
            team_dict[team1], team_dict[team2] = env.rate_1vs1(team_dict[team1], team_dict[team2])
        else:
            team_dict[team2], team_dict[team1] = env.rate_1vs1(team_dict[team2], team_dict[team1])


env = Glicko2(tau=0.5)
secret = "Secret"
alliance = "Alliance"
navi = "NaVi"
og = "OG"
liquid = "Liquid"
vp = "VP"
nigma = "Nigma"
vikingg = "Vikin.gg"
mudgolems = "Mudgolems"
error = "Just Error"

team_dict = {
                secret:env.create_rating(1500, 40),
                alliance:env.create_rating(1500, 40),
                navi:env.create_rating(1500, 40),
                og:env.create_rating(1500, 40),
                liquid:env.create_rating(1500, 40),
                vp:env.create_rating(1500, 40),
                nigma:env.create_rating(1500, 40),
                vikingg:env.create_rating(1500, 40),
                mudgolems:env.create_rating(1500, 40),
                error:env.create_rating(1500, 40)
            }

### DAY 1
compute_series(team_dict, [vp, og, [1, 1]])
compute_series(team_dict, [navi, liquid, [0, 1, 1]])
compute_series(team_dict, [mudgolems, error, [1, 0, 1]])

### DAY 2
compute_series(team_dict, [vikingg, liquid, [1, 0, 1]])
compute_series(team_dict, [secret, mudgolems, [1, 0, 1]])
compute_series(team_dict, [og, alliance, [1, 0, 1]])

### DAY 3
compute_series(team_dict, [navi, error, [1, 0, 1]])
compute_series(team_dict, [vikingg, secret, [1, 1]])
compute_series(team_dict, [mudgolems, nigma, [0, 1, 1]])

### DAY 4
compute_series(team_dict, [error, liquid, [1, 1]])
compute_series(team_dict, [navi, alliance, [1, 0, 1]])
compute_series(team_dict, [nigma, og, [0, 1, 1]])

### DAY 5
compute_series(team_dict, [vp, error, [0, 1, 1]])
compute_series(team_dict, [vikingg, mudgolems, [0, 1, 1]])
compute_series(team_dict, [nigma, alliance, [1, 1]])

### DAY 6
compute_series(team_dict, [vikingg, og, [1, 1]])
compute_series(team_dict, [nigma, error, [1, 1]])
compute_series(team_dict, [secret, liquid, [1, 1]])

### DAY 7
compute_series(team_dict, [vp, mudgolems, [1, 1]])
compute_series(team_dict, [alliance, vikingg, [1, 1]])
compute_series(team_dict, [secret, error, [1, 1]])

### DAY 8
compute_series(team_dict, [og, navi, [1, 1]])
compute_series(team_dict, [liquid, alliance, [1, 1]])
compute_series(team_dict, [vp, nigma, [1, 1]])

### DAY 9
### DAY 10
### DAY 11
### DAY 12
### DAY 13
### DAY 14
### DAY 15


team_scores = []
for key in team_dict:
    team_scores.append([key, team_dict[key].mu])
team_scores = sorted(team_scores, key=lambda x: x[1], reverse=True)

print("EPIC League glicko-2 ratings:")
for idx, team in enumerate(team_scores):
    print("\t{:>2}. {:<14} {:6.0f}".format(idx+1, team[0], team[1]))