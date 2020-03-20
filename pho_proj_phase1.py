
import requests
import json
from ratelimit import limits, sleep_and_retry

RATE = 5

accountSet = set([])
set2 = set([])
matches = {}
matches['matchId'] = []
data = {}
data['matches'] = []
matchInfo = {}
matchInfo['info'] = []
xd = {}
xd['data'] = []

def getSummonerData(region, summonerName, APIKey):
	URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
	response = requests.get(URL)
	return response.json()

@sleep_and_retry
@limits(calls=2, period=RATE)
def getMatchList(region, accountId, APIKey):
	URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?api_key=" + APIKey
	response = requests.get(URL)
	return response.json(), response.status_code

@sleep_and_retry
@limits(calls=2, period=RATE)
def getMatchInfo(region, gameId, APIKey):
	URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matches/" + gameId + "?api_key=" + APIKey
	response = requests.get(URL)
	return response.json(), response.status_code

@sleep_and_retry
@limits(calls=4, period=RATE)
def getMatch(region, matchId, APIKey):
	URL = "https://" + region + ".api.riotgames.com/lol/match/v4/timelines/by-match/" + matchId + "?api_key=" + APIKey
	response = requests.get(URL)
	return response.json(), response.status_code

def update(region, accountId, APIKey):
	matchListJSON, code = getMatchList(region, accountId, APIKey)
	if code != 200:
		return
	for x in matchListJSON['matches']:
		matches['matchId'].append(x['gameId'])
	data['matches'].append(matchListJSON)
	gameId = matchListJSON['matches'][0]['gameId']
	gameId = str(gameId)

	matchInfoJSON, code = getMatchInfo(region, gameId, APIKey)
	if code != 200:
		return

	tempSet = set([])
	for x in matchInfoJSON['participantIdentities']:
		tempSet.add(x['player']['accountId'])
	set2.update(tempSet.difference(accountSet))
	print("ran")

def main():
	region = "na1"
	summonerName = "Setsuji"
	APIKey = "RGAPI-04d78180-862e-42f3-8493-55334b244b91"

	responseJSON = getSummonerData(region, summonerName, APIKey)
	
	accountId = responseJSON['accountId']
	accountId = str(accountId)
	accountSet.add(accountId)	
	
	set2.add(accountId)

	#while(bool(set2)):
	for x in range(0, 1):
		print(x)
		setTemp = set2.copy()
		set2.clear()
		for x in setTemp:
			print("run")
			update(region, x, APIKey)
		accountSet.update(set2)
	with open('deletethis.json', 'w') as outfile:
		json.dump(data, outfile)
	print("EXPORTED FIRST FILE")
	for y in matches['matchId']:
		print(y)
		a, code = getMatch(region, str(y), APIKey)
		print(code)
		if code != 200:
			continue
		xd['data'].append(a)
	print(xd)
	with open('gameTimelineSample.json', 'w') as outfile:
		json.dump(xd, outfile)
	print("FINISHED!")

if __name__ == "__main__":
	main()
