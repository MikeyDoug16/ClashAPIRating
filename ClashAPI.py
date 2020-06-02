import json
import urllib.parse
import urllib.request
import sys
#import requests

#CLASH_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhmYjRjZDNmLTlmNDktNDM4Ny04OWJlLTgyMzQ4NTc0NjE2MiIsImlhdCI6MTU1ODY0ODY3Niwic3ViIjoiZGV2ZWxvcGVyLzgxNTJlMjYzLTg4ZmQtZDY1Zi05NWI2LWRiNzY0NTgzYTQ5MCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjk4LjE4MC4xNDcuMTUwIl0sInR5cGUiOiJjbGllbnQifV19.ozDaUqoxAwFBBfh5Yl5q5iWJ1LLEymXKfSMiPgKOcz-b9vIcax0VxIYNf8LPCmgr5ho3DLgwPk5cXf9vpfyjoA"
HOME_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjgxMjViMDM3LTc4Y2MtNGI2MS1hMGExLTdmM2Q3NTc2MzM4ZSIsImlhdCI6MTU4NTk4NTEyOSwic3ViIjoiZGV2ZWxvcGVyLzgxNTJlMjYzLTg4ZmQtZDY1Zi05NWI2LWRiNzY0NTgzYTQ5MCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE3Mi4yNTEuNTYuMzciXSwidHlwZSI6ImNsaWVudCJ9XX0.5WGtMQ-t9A3-eklu9eMTup7wPmEFTvYNNulgp5BJVgF8bHuXO7H3PaVsMUPRRngHeJtoLcpxfhDsVp2VpZ0g5A'
#CLASH_NAME = "https://api.clashofclans.com/v1/clans/%23QG9C2GR?Authorization=Bearer"+CLASH_TOKEN
CLASH_NAME="https://api.clashofclans.com/v1"
HEADER = {'authorization': 'Bearer '+HOME_TOKEN, 'Accept': 'application/json'}
TROOP_SCORE = {'Barbarian': [0,0,0,0,0,0], 'Archer':[0,0,0,0,0,0], 'Goblin':[0,0,0,0,0,0], 'Giant':[0,0,0,0,0,0], 'Wall Breaker':[3,1,0,0,0,0], 'Balloon':[1,2,1,3,4,4],
               'Wizard':[4,3,3,0,3,2], 'Healer':[0,2,1,2,3,2], 'Dragon':[1,1,1,1,1,1], 'P.E.K.K.A':[2,1,1,0,1,0], 'Minion':[0,1,0,1,1,0], 'Hog Rider':[3,2,2,0,0,1],
               'Valkyrie':[1,0,0,0,0,0], 'Golem':[3,3,2,0,0,0], 'Witch':[-1,2,2,1,0,1], 'Lava Hound':[-1,1,0,1,0,0], 'Bowler':[-1,-1,1,0,3,1], 'Baby Dragon':[-1,0,1,1,3,1],
               'Miner':[-1,-1,0,1,1,1], 'Wall Wrecker':[-1,-1,-1,-1,5,5], 'Battle Blimp':[-1,-1,-1,-1,2,2], 'Yeti':[-1,-1,-1,-1,1,2], 'Ice Golem':[-1,-1,-1,3,1,1],
               'Electro Dragon':[-1,-1,-1,3,1,1], 'Stone Slammer':[-1,-1,-1,-1,3,3], 'Siege Barracks':[-1,-1,-1,-1,-1,3], 'Lightning Spell':[1,0,1,0,0,0], 
               'Healing Spell':[4,3,4,1,1,1], 'Rage Spell':[4,4,5,5,5,5], 'Jump Spell':[-1,2,1,1,1,0], 'Freeze Spell':[-1,0,4,3,4,4],
               'Poison Spell':[5,5,3,2,3,3], 'Earthquake Spell':[0,2,0,0,1,1], 'Haste Spell':[-1,2,1,2,1,0], 'Clone Spell':[-1,-1,0,1,0,1],
               'Skeleton Spell':[-1,1,0,0,0,0], 'Bat Spell':[-1,-1,0,2,0,1]}
TH8BASE = 129
TH9BASE = 192
TH10BASE = 278
TH11BASE = 323
TH12BASE = 475
TH13BASE = 575


def result() ->str:
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text=response.read().decode(encoding='utf-8')
        print(json_text)
        return json.loads(json_text)
    except:
        return None
    finally:
        if response != None:
            response.close()


def contact(tag) -> list:
    parameters =[]
    #parameters.append(()) <- Use parameters if you want to search specific clans I.e parameters.append(('name', '+34')) +34 is my clan 
    #uri = "/players/%23LQUJPLUG"
    #uri = "/players/%239V2PRCVUP"
    uri = "/players/%23"+tag
    #uri = "/players/%efewfewfwefefewfw"
    #uri = "/players/%23LQROYG2UL"
    URL = CLASH_NAME + uri + '?' + urllib.parse.urlencode(parameters)
    try:
        req = urllib.request.Request(URL, headers = HEADER)
        response = urllib.request.urlopen(req)
        json_text=response.read().decode(encoding='utf-8')
        json_dict= json.loads(json_text)
        result_list = [json_dict['troops'], json_dict['heroes'], json_dict['spells'],json_dict['tag'],json_dict['name'], json_dict['townHallLevel']]
        return result_list
    except:
        return []

def count(troops) -> int:
    c = 0
    for dicts in troops:
        if dicts['village'] != 'builderBase':
            c+=1
    return c

def build_list(dicts)->list:
    res = []
    for items in dicts:
        if items['village'] != 'builderBase' and 'Super' not in items['name'] and 'Sneaky' not in items['name']:
            res.append(items)
    return res

def CalcTHScore(troops, heroes, spells,thlevel) -> int:
    res = 0
    for troop in troops:
        res = res + (troop['level'] * (1 + TROOP_SCORE[troop['name']][thlevel-8]))
    for spell in spells:
        res = res + (spell['level'] * (1 + TROOP_SCORE[spell['name']][thlevel-8]))
    for hero in heroes:
        res += hero['level']
    return res

def troop_score(troops, heroes, spells, townHallLevel) -> int:
    if townHallLevel >= 8:
        return CalcTHScore(troops, heroes, spells,townHallLevel)
    else:
        print("ERROR Invalid Town Hall Level. This program only works on town halls 8-12 as most clans do not accept sub town hall 8s unless they've know them previously.")
        print("Please try again with a new player whose town hall falls within the accepted range. Sorry for any inconvenience.")
        sys.exit()

def check_score(score, townhall_level):
    if townhall_level == 8:
        if score >= TH8BASE:
            print("This player is above the recommended minimum score for a Town Hall level 8 player. Their troops are satisfactory" +
                  " and ultimately they should be accepted into your clan, provided their base is also up to standard.")
        else:
            print("This player's score is below the recommended minimum score for a Town Hall level 8 player. This player most likely" +
                    " rushed their town hall and unfortunately should not be accepted into your clan.")
    elif townhall_level == 9:
        if score >= TH9BASE:
            print("This player is above the recommended minimum score for a Town Hall level 9 player. Their troops are satisfactory" +
                  " and ultimately they should be accepted into your clan, provided their base is also up to standard.")
        else:
            print("This player's score is below the recommended minimum score for a Town Hall level 9 player. This player most likely" +
                    " rushed their town hall and unfortunately should not be accepted into your clan.")
    elif townhall_level == 10:
        if score >= TH10BASE:
            print("This player is above the recommended minimum score for a Town Hall level 10 player. Their troops are satisfactory" +
                  " and ultimately they should be accepted into your clan, provided their base is also up to standard.")
        else:
            print("This player's score is below the recommended minimum score for a Town Hall level 10 player. This player most likely" +
                    " rushed their town hall and unfortunately should not be accepted into your clan.")
    elif townhall_level == 11:
        if score >= TH11BASE:
            print("This player is above the recommended minimum score for a Town Hall level 11 player. Their troops are satisfactory" +
                  " and ultimately they should be accepted into your clan, provided their base is also up to standard.")
        else:
            print("This player's score is below the recommended minimum score for a Town Hall level 11 player. This player most likely" +
                    " rushed their town hall and unfortunately should not be accepted into your clan.")
    elif townhall_level == 12:
        if score >= TH12BASE:
            print("This player is above the recommended minimum score for a Town Hall level 12 player. Their troops are satisfactory" +
                  " and ultimately they should be accepted into your clan, provided their base is also up to standard.")
        else:
            print("This player's score is below the recommended minimum score for a Town Hall level 12 player. This player most likely" +
                    " rushed their town hall and unfortunately should not be accepted into your clan.")
    elif townhall_level == 13:
        if score >= TH13BASE:
            print("This player is above the recommended minimum score for a Town Hall level 13 player. Their troops are satisfactory" +
                  " and ultimately they should be accepted into your clan, provided their base is also up to standard.")
        else:
            print("This player's score is below the recommended minimum score for a Town Hall level 13 player. This player most likely" +
                    " rushed their town hall and unfortunately should not be accepted into your clan.")
def begin_troop_processing(troops) -> (int,int):
    home_troops = build_list(troops[0])
    home_heroes = build_list(troops[1])
    home_spells = build_list(troops[2])
    score = 0
    print("Calculating score for " + troops[4] + ". Player tag is: " + troops[3] + " and Player town hall is: " + str(troops[5]))
    score += troop_score(home_troops, home_heroes, home_spells, troops[5])
    print("Score is: " + str(score))
    return (score, int(troops[5]))

def print_opening()->None:
    print("----------------------------------------------------------------------------------------------")
    print("-                 Welcome to the Clash of Clans Player Rating Program                        -")
    print("-     Here you can find the rating of a player based on their troops, heroes and spells      -")
    print("-    You will need a player tag (MAKE SURE IT IS VALID OR IT WILL NOT WORK) [NO Hashtag]     -")
    print("-        The rating provided will be based on the meta (what's popular) of the game          -")
    print("- You can use this rating to see matchups in war or if a player is high enough for your clan -")
    print("-    The rating will be tested against a baseline rating to check for rushing a town hall    -")
    print("-            So let us begin and lets find out the ratings you are looking for               -")
    print("----------------------------------------------------------------------------------------------")

def get_tag()->str:
    tag = input("Please enter the tag here [NO HASHTAG]: ")
    return tag

def get_type()->str:
    print("First pick the type of ratings. You can do a single player rating (rating for one player) or you can do full war ratings.")
    print("Full War Ratings will ask for both FULL teams (TH8+) and show you the full player rating matchups.")    
    s = ""
    while s != "W" and s!= "w" and s != "P" and s != "p":
        s = input("Please enter P/p for a single player rating or W/w for a War matchup rating: ")
    return s

def team_rating(team, size, num_team)->list:
    print("Beginning the tag entering stage for team " + num_team + "...")
    for i in range(size):
        troop_data = []
        while True:
            tag = get_tag()
            if tag == "7" or tag == "6" or tag == "5" or tag == "4" or tag == "3":
                team.append((int(tag), 0))
                break
            else:
                troop_data = contact(tag)
                if troop_data == []:
                    print("ERROR! Sorry that is an invalid tag. Please make sure the tag you enter is correct without the hashtag [#] at the front")
                else:
                    score_th = begin_troop_processing(troop_data)
                    team.append((score_th[1],score_th[0]))
                    break
    return team

def war_rating():
    size = 0
    while size <= 4 or size >= 51:
        try:
            size = int(input("First we need to know the size of the teams for War. Put the size 5-50 in increments of 5, i.e 5,10,15,...,50: "))
        except:
            continue
    team1 = []
    team2 = []
    print("Now we will ask for the player tags of the " + str(size) + " members of each team in order from #1 to " + str(size))
    print("If they are Town hall 7 or below put their Town Hall number only as this will not give them a rating since this is a TH8+ rating system.")
    team1 = team_rating(team1,size, "1")
    team2 = team_rating(team2,size, "2")
    print("\n\n")
    print("Here are the matchup ratings for the clan war. Any Town Hall below 8 receives a score of 0 by default.")
    for i in range(1,size+1):
          print("Matchup " + str(i) + ": Town Hall " + str(team1[i-1][0]) + ", Score " + str(team1[i-1][1]) + " vs Town Hall " + str(team2[i-1][0]) + ", Score " + str(team2[i-1][1]))
    
def single_rating():
    while True:
        tag = get_tag()
        #troop_data = contact("9Y08PUJL8") #th8
        #troop_data = contact("28L89L9PV") #th9
        #troop_data = contact("R8R92JCG") #th10
        #troop_data = contact("YPQVJQ2P") #th11 me :)
        #troop_data = contact("GLV20JQL") #th12
        #troop_data = contact("LQUJPLUG")#th13
        troop_data = contact(tag)
        if troop_data == []:
            print("ERROR! Sorry that is an invalid tag. Please make sure the tag you enter is correct without the hashtag [#] at the front")
        else:
            break
    score_th = begin_troop_processing(troop_data)
    check_score(score_th[0],score_th[1])
if __name__ == '__main__':
    print_opening()
    print()
    ty = get_type()
    if ty == 'P' or ty == 'p':
        single_rating()
    else:
        war_rating()


        
