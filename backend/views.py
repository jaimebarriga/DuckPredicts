from django.shortcuts import render_to_response
from django.template import RequestContext
from consts import WC_COUNTRIES
from django.http import HttpResponseBadRequest, \
    HttpResponseRedirect, HttpResponseServerError, HttpResponseNotFound, \
    HttpResponse

# Create your views here.
def index(request):
	return render_to_response('index.html', {
		"WC_COUNTRIES": WC_COUNTRIES
	}, context_instance=RequestContext(request))

def winner(request):
	try:
		team1 = request.POST['team1']
		team2 = request.POST['team2']
		print ("%s versus %s" % (team1, team2))
	except:
		pass

	return render_to_response('winner.html', {
		"team1": team1, "team2": team2
	}, context_instance=RequestContext(request))
