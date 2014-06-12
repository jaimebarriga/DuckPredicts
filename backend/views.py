from django.shortcuts import render_to_response
from django.template import RequestContext
from consts import WC_COUNTRIES, TEAM_RANKINGS
from django.http import HttpResponseBadRequest, \
    HttpResponseRedirect, HttpResponseServerError, HttpResponseNotFound, \
    HttpResponse
import pdb, random

# Create your views here.
def index(request):
	return render_to_response('index.html', {
		"WC_COUNTRIES": WC_COUNTRIES
	}, context_instance=RequestContext(request))

def winner(request):
	try:
		team1 = str(request.POST['team1'])
		team2 = str(request.POST['team2'])
		print ("%s versus %s" % (team1, team2))
	except:
		pass

	team1value = TEAM_RANKINGS[team1.upper()]
	team2value = TEAM_RANKINGS[team2.upper()]

	if(team1value > team2value):
		team1winpercent = 55 - (team1value - team2value)
		team1winbool = random.randrange(100) < team1winpercent
		if(team1winbool):
			WINNER = team1.upper()
		else:
			WINNER = team2.upper()

	else:
		team2winpercent = 55 - (team2value - team1value)
		team2winbool = random.randrange(100) < team2winpercent
		if(team2winbool):
			WINNER = team2.upper()
		else:
			WINNER = team1.upper()


	return render_to_response('winner.html', {
		"team1": team1, "team2": team2, "WINNER":WINNER
	}, context_instance=RequestContext(request))
